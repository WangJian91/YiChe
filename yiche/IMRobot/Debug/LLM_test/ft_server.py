import asyncio
import uvloop
from sanic import Sanic
from sanic.response import json
import time
from transformers import LlamaTokenizer
from torch.nn.utils.rnn import pad_sequence
import numpy as np
import torch
import google.protobuf.json_format
import json
import queue
import threading
import tritonclient.grpc as grpcclient
from functools import partial
from tritonclient.grpc.service_pb2 import ModelInferResponse
from tritonclient.utils import np_to_triton_dtype
import random
import datetime
import os

from loggeruru import Logger
alogger = Logger().get_logger
dlogger = alogger.bind(reqid='None').bind(user="None").bind(web=True)


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


log_prefix = "vicuna v1.5 16k model infer: "
model_name = "vicuna-13b-v1.5-16k"
port = 17862
workers_num = 8
evn = os.getenv('SERVER_ENV')


with open("sample_request_stream.json", "r") as f:
    default_data = json.load(f)
dlogger.info(f"{log_prefix}default_data: {default_data}")

app = Sanic("WebSocketTest")


def to_word_list_format(token_ids_list):
    if token_ids_list is None:
        return np.array([[[0], [-1]]], dtype="int32")
    flat_ids = []
    offsets = []

    item_flat_ids = []
    item_offsets = []
    for token_ids in token_ids_list:
        item_flat_ids += token_ids
        item_offsets.append(len(token_ids))
    flat_ids.append(np.array(item_flat_ids))
    offsets.append(np.cumsum(np.array(item_offsets)))

    pad_to = max(1, max(len(ids) for ids in flat_ids))

    for i, (ids, offs) in enumerate(zip(flat_ids, offsets)):
        flat_ids[i] = np.pad(ids, (0, pad_to - len(ids)), constant_values=0)
        offsets[i] = np.pad(offs, (0, pad_to - len(offs)), constant_values=-1)

    return np.array([flat_ids, offsets], dtype="int32").transpose((1, 0, 2))


def prepare_tensor(client, name, input):
    t = client.InferInput(name, input.shape, np_to_triton_dtype(input.dtype))
    t.set_data_from_numpy(input)
    return t


class LlamaTritonClient:
    def __init__(self):
        self.tokenizer = LlamaTokenizer.from_pretrained('lmsys/vicuna-13b-v1.5-16k')
        self.start_id = self.tokenizer.bos_token_id
        self.end_id = self.tokenizer.eos_token_id
        dlogger.info(f"{log_prefix}start id: {self.start_id} end id: {self.end_id}")

    def stream_callback(self, result_queue, request_input_len, max_output_len, return_log_probs, result, error):
        # if error:
        #     queue.put(error)
        # else:
        #     queue.put(result.get_response(as_json=True))
        # print("stream_callback", datetime.datetime.now())
        message = ModelInferResponse()
        google.protobuf.json_format.Parse(json.dumps(result.get_response(as_json=True)), message)
        result = grpcclient.InferResult(message)

        idx = result.as_numpy("sequence_length")[0, 0]
        is_finish = result.as_numpy("finished").tolist()[0][0]
        # print("finish", type(is_finish), is_finish)
        # print("idx", idx)
        # print(result.as_numpy("output_ids")[0, 0, :])
        tokens = result.as_numpy("output_ids")[0, 0, request_input_len:idx]
        # print(tokens)
        # is_finish = False
        # try:
        #     result_text = self.tokenizer.decode(tokens)
        #     # 目前只能是5
        #     _max_width = max_output_len % 5
        #     is_finish = True if tokens[-1] == self.end_id or len(
        #         tokens) >= max_output_len - request_input_len - _max_width else False
        #     # if stop_words:
        #     #     for stop_word in stop_words:
        #     #         if stop_word in result_text:
        #     #             is_finish = True
        #     #             result_text = "".join(result_text.split(stop_word)[:-1])
        #     #             break
        #     if is_finish:
        #         result_text = result_text.rstrip(self.tokenizer.eos_token)
        # except:
        #     result_text = ""
        result_text = self.tokenizer.decode(tokens)
        # 目前只能是5
        _max_width = max_output_len % 5
        is_finish = True if tokens[-1] == self.end_id or len(tokens) >= max_output_len - request_input_len - _max_width else False
        # if stop_words:
        #     for stop_word in stop_words:
        #         if stop_word in result_text:
        #             is_finish = True
        #             result_text = "".join(result_text.split(stop_word)[:-1])
        #             break
        if is_finish:
            result_text = result_text.rstrip(self.tokenizer.eos_token)
        result_json = {
            "result": {
                "text": result_text,
            },
            "usage": {
                "promptTokens": request_input_len,
                "completionTokens": len(tokens),
                "totalTokens": len(tokens) + request_input_len
            },
            "finish": is_finish
        }
        # if return_log_probs:
        #     prob = result.as_numpy("cum_log_probs")
        #     output_prob = result.as_numpy("output_log_probs")
        #     print(prob, output_prob.shape)
        #     result_json["result"]["logprobs"] = prob
        result_queue.put(result_json)

    def grpc_stream(self, request, request_input_len, max_output_len, return_log_probs, result_queue):
        with grpcclient.InferenceServerClient(default_data['config']['url'],
                                              verbose=default_data['config']["verbose"]) as cl:
            payload = [prepare_tensor(grpcclient, item_name, request[item_name])
                       for item_name in request]
            cl.start_stream(callback=partial(self.stream_callback, result_queue, request_input_len, max_output_len, return_log_probs))
            # result_queue.put(time.perf_counter())
            cl.async_stream_infer(default_data['config']['model_name'], payload)
        # result_queue.put(None)
        # consumer.join()

    def create_request(self, query):
        """
            query : batch string (2D numpy array)
        """
        start_ids = [torch.IntTensor(self.tokenizer.encode(s[0])) for s in query]
        start_lengths = torch.IntTensor([[len(ids)] for ids in start_ids])

        start_ids = pad_sequence(start_ids, batch_first=True, padding_value=self.end_id)

        return start_ids, start_lengths

    def run(self, new_request_json, return_log_probs, result_queue):
        self.grpc_stream(new_request_json, len(new_request_json["input_ids"][0]),
                         new_request_json["request_output_len"][0][0], return_log_probs, result_queue)
        result_queue.put({"finish": True})


llama_triton_client = LlamaTritonClient()


def default_dump(obj):
    """Convert numpy classes to JSON serializable objects."""
    if isinstance(obj, (np.integer, np.floating, np.bool_)):
        return obj.item()
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return obj


# async def main_logic(websocket, path):
async def main_logic(request, websocket):
    # print("main_logic start: ", datetime.datetime.now())
    data = await websocket.recv()
    result_queue = queue.Queue()
    # logger.info(f"[kafka log]: {log_prefix}triton_client.run start")
    re_data = {'code': 9999, "message": "", 'result': {'text': '', 'index': -1},
           'usage': {'promptTokens': -1, 'completionTokens': -1, 'totalTokens': -1},
           'finish': True}

    request_json = json.loads(data)
    if "userId" not in request_json.keys():
        re_data["message"] = "userId not in request data param"
        await websocket.send(json.dumps(re_data,
                                        ensure_ascii=False, default=default_dump))
        await websocket.send("close")
        return
    else: user_ids = request_json["userId"]

    if "requestId" not in request_json.keys():
        re_data["message"] = "requestId not in request data param"
        await websocket.send(json.dumps(re_data,
                                        ensure_ascii=False, default=default_dump))
        await websocket.send("close")
        return
    else: request_ids = request_json["requestId"]

    if "prompt" not in request_json.keys():
        re_data["message"] = "prompt not in request data param"
        await websocket.send(json.dumps(re_data,
                                        ensure_ascii=False, default=default_dump))
        await websocket.send("close")
        return
    else: prompt = request_json["prompt"]

    logger = alogger.bind(reqid=request_ids).bind(user=user_ids).bind(web=True)
    logger.info(f"{log_prefix}triton_client.run start")
    logger.info(f"{log_prefix}request_json: {request_json}")
    use_stream = request_json["stream"] if "stream" in request_json.keys() else False
    # print("main_logic data load end: ", datetime.datetime.now())

    # step 1 input convert
    query = np.array([[request_json["prompt"]]], dtype=object)
    return_log_probs = request_json["logprobs"] if "logprobs" in request_json.keys() else 0
    bad_words_ids = request_json["badWordsIds"] if "badWordsIds" in request_json.keys() else None
    stop_words_ids = request_json["stopWordsIds"] if "stopWordsIds" in request_json.keys() else None
    input_id, request_input_len = llama_triton_client.create_request(query)
    bad_words = to_word_list_format(bad_words_ids)
    stop_words = to_word_list_format(stop_words_ids)
    new_request_json = {
        "input_ids": np.array(input_id, "uint32"),
        "input_lengths": np.array(request_input_len, "uint32"),
        "bad_words_list": np.array(bad_words, "int32"),
        "stop_words_list": np.array(stop_words, "int32"),
    }
    if "useRandom" in request_json.keys() and not request_json["useRandom"]:
        new_request_json["random_seed"] = np.array([[0]], dtype="uint64")
    else:
        new_request_json["random_seed"] = np.array([[random.randint(0, 100000)]], dtype="uint64")
    for item in default_data["request"]:
        common_name = item["common_name"] if "common_name" in item else item["name"]
        if common_name == "is_return_log_probs":
            if return_log_probs > 0:
                new_request_json[item["name"]] = np.array([[True]], dtype=item['dtype'])
            continue
        if common_name == "maxTokens":
            maxTokens = request_json["maxTokens"]
            if int(maxTokens) > item["data"]:
                re_data["message"] = "maxTokens in request data param is out of range {}".format(item["data"])
                await websocket.send(json.dumps(re_data,
                                                ensure_ascii=False, default=default_dump))
                await websocket.send("close")
                return
        if common_name in request_json.keys():
            new_request_json[item["name"]] = np.array([[request_json[common_name]]], dtype=item['dtype'])
        else:
            new_request_json[item["name"]] = np.array([[item['data']]], dtype=item['dtype'])
    logger.info(f"{log_prefix}new_request_json: {new_request_json}")
    # print("main_logic input data load: ", datetime.datetime.now())

    # step 2 grpc thread
    product = threading.Thread(target=llama_triton_client.run, args=(new_request_json, return_log_probs, result_queue))
    product.start()
    logger.info(f"{log_prefix}triton_client.run start")
    g_index = 0
    last_re_data = None
    # print("main_logic thread begin: ", datetime.datetime.now())

    # step 3 ws push
    while True:
        re_data = result_queue.get()
        logger.info(f"{log_prefix}re_data: {re_data}")
        re_data["code"] = 0
        re_data["message"] = ""
        if "result" in re_data: re_data["result"]["index"] = g_index
        # await websocket.send(re_data.lstrip("<s>").rstrip("</s>"))
        if re_data["finish"]:
            if "result" not in re_data and "result" in last_re_data:
                re_data["result"] = last_re_data["result"]
                if "usage" in last_re_data:
                    re_data["usage"] = last_re_data
            await websocket.send(json.dumps(re_data, ensure_ascii=False, default=default_dump))
            logger.info(f"{log_prefix} streamer finished")
            break
        else:
            last_re_data = re_data
            if use_stream:
                await websocket.send(json.dumps(re_data, ensure_ascii=False, default=default_dump))
        g_index += 1
    await websocket.send("close")
    # print("main_logic end: ", datetime.datetime.now())

    # step 4 kafka data load
    kafka_info = {
        "model_name": model_name,
        "userId": user_ids,
        "requestId": request_ids,
        "prompt": prompt,
        "stream": use_stream,
        "logprobs": return_log_probs,
        "badWordsIds": bad_words_ids,
        "stopWordsIds": stop_words_ids,
        "useRandom": request_json["useRandom"] if "useRandom" in request_json.keys() else True,
        "randomSeed": new_request_json["random_seed"][0][0],
        "runtimeTopK": new_request_json["runtime_top_k"][0][0],
        "runtimeTopP": new_request_json["runtime_top_p"][0][0],
        "beamWidth": new_request_json["beam_width"][0][0],
        "repetitionPenalty": new_request_json["repetition_penalty"][0][0],
        "lenPenalty": new_request_json["len_penalty"][0][0],
        "temperature": new_request_json["temperature"][0][0],
        "beamSearchDiversityRate": new_request_json["beam_search_diversity_rate"][0][0],
        "startId": llama_triton_client.start_id,
        "endId": llama_triton_client.end_id,
        "requestOutputLen": new_request_json["request_output_len"][0][0],
        "inputLengths": new_request_json["input_lengths"][0][0],
        "inputIds": str(new_request_json["input_ids"][0].tolist()),
        "badWordsList": str(new_request_json["bad_words_list"][0].tolist()),
        "stopWordsList": str(new_request_json["stop_words_list"][0].tolist()),
        "text": re_data["result"]["text"] if "result" in re_data.keys() and "text" in re_data["result"].keys() else "",
        "index": re_data["result"]["index"] if "result" in re_data.keys() and "index" in re_data["result"].keys() else -1,
        "promptTokens": re_data["usage"]["promptTokens"] if "usage" in re_data.keys() and "promptTokens" in re_data["usage"].keys() else new_request_json["input_lengths"][0][0],
        "completionTokens": re_data["usage"]["completionTokens"] if "usage" in re_data.keys() and "completionTokens" in re_data["usage"].keys() else 0,
        "totalTokens": re_data["usage"]["totalTokens"] if "usage" in re_data.keys() and "totalTokens" in re_data["usage"].keys() else new_request_json["input_lengths"][0][0],
        "finish": re_data["finish"] if "finish" in re_data.keys() else False,
        "success": True
    }
    if evn == "online": logger.info(f"[kafka log]: {log_prefix}kafka_info data={kafka_info}")
    logger.info(f"{log_prefix}triton_client.run close")
    del result_queue
    # print("main_logic kafka push: ", datetime.datetime.now())


@app.websocket('/llm/ft_vicuna_16k')
async def feed(request, websocket):
    # print("main_logic start: ", datetime.datetime.now())
    data = await websocket.recv()
    result_queue = queue.Queue()
    # logger.info(f"[kafka log]: {log_prefix}triton_client.run start")
    re_data = {'code': 9999, "message": "", 'result': {'text': '', 'index': -1},
           'usage': {'promptTokens': -1, 'completionTokens': -1, 'totalTokens': -1},
           'finish': True}

    request_json = json.loads(data)
    if "userId" not in request_json.keys():
        re_data["message"] = "userId not in request data param"
        await websocket.send(json.dumps(re_data,
                                        ensure_ascii=False, default=default_dump))
        await websocket.send("close")
        return
    else: user_ids = request_json["userId"]

    if "requestId" not in request_json.keys():
        re_data["message"] = "requestId not in request data param"
        await websocket.send(json.dumps(re_data,
                                        ensure_ascii=False, default=default_dump))
        await websocket.send("close")
        return
    else: request_ids = request_json["requestId"]

    if "prompt" not in request_json.keys():
        re_data["message"] = "prompt not in request data param"
        await websocket.send(json.dumps(re_data,
                                        ensure_ascii=False, default=default_dump))
        await websocket.send("close")
        return
    else: prompt = request_json["prompt"]

    logger = alogger.bind(reqid=request_ids).bind(user=user_ids).bind(web=True)
    logger.info(f"{log_prefix}triton_client.run start")
    logger.info(f"{log_prefix}request_json: {request_json}")
    use_stream = request_json["stream"] if "stream" in request_json.keys() else False
    # print("main_logic data load end: ", datetime.datetime.now())

    # step 1 input convert
    query = np.array([[request_json["prompt"]]], dtype=object)
    return_log_probs = request_json["logprobs"] if "logprobs" in request_json.keys() else 0
    bad_words_ids = request_json["badWordsIds"] if "badWordsIds" in request_json.keys() else None
    stop_words_ids = request_json["stopWordsIds"] if "stopWordsIds" in request_json.keys() else None
    input_id, request_input_len = llama_triton_client.create_request(query)
    bad_words = to_word_list_format(bad_words_ids)
    stop_words = to_word_list_format(stop_words_ids)
    new_request_json = {
        "input_ids": np.array(input_id, "uint32"),
        "input_lengths": np.array(request_input_len, "uint32"),
        "bad_words_list": np.array(bad_words, "int32"),
        "stop_words_list": np.array(stop_words, "int32"),
    }
    if "useRandom" in request_json.keys() and not request_json["useRandom"]:
        new_request_json["random_seed"] = np.array([[0]], dtype="uint64")
    else:
        new_request_json["random_seed"] = np.array([[random.randint(0, 100000)]], dtype="uint64")
    for item in default_data["request"]:
        common_name = item["common_name"] if "common_name" in item else item["name"]
        if common_name == "is_return_log_probs":
            if return_log_probs > 0:
                new_request_json[item["name"]] = np.array([[True]], dtype=item['dtype'])
            continue
        if common_name == "maxTokens":
            maxTokens = request_json["maxTokens"]
            if int(maxTokens) > item["data"]:
                re_data["message"] = "maxTokens in request data param is out of range {}".format(item["data"])
                await websocket.send(json.dumps(re_data,
                                                ensure_ascii=False, default=default_dump))
                await websocket.send("close")
                return
        if common_name in request_json.keys():
            new_request_json[item["name"]] = np.array([[request_json[common_name]]], dtype=item['dtype'])
        else:
            new_request_json[item["name"]] = np.array([[item['data']]], dtype=item['dtype'])
    logger.info(f"{log_prefix}new_request_json: {new_request_json}")
    # print("main_logic input data load: ", datetime.datetime.now())

    # step 2 grpc thread
    product = threading.Thread(target=llama_triton_client.run, args=(new_request_json, return_log_probs, result_queue))
    product.start()
    logger.info(f"{log_prefix}triton_client.run start")
    g_index = 0
    last_re_data = None
    # print("main_logic thread begin: ", datetime.datetime.now())

    # step 3 ws push
    while True:
        re_data = result_queue.get()
        logger.info(f"{log_prefix}re_data: {re_data}")
        re_data["code"] = 0
        re_data["message"] = ""
        if "result" in re_data: re_data["result"]["index"] = g_index
        # await websocket.send(re_data.lstrip("<s>").rstrip("</s>"))
        if re_data["finish"]:
            if "result" not in re_data and "result" in last_re_data:
                re_data["result"] = last_re_data["result"]
                if "usage" in last_re_data:
                    re_data["usage"] = last_re_data
            await websocket.send(json.dumps(re_data, ensure_ascii=False, default=default_dump))
            logger.info(f"{log_prefix} streamer finished")
            break
        else:
            last_re_data = re_data
            if use_stream:
                await websocket.send(json.dumps(re_data, ensure_ascii=False, default=default_dump))
        g_index += 1
    await websocket.send("close")
    # print("main_logic end: ", datetime.datetime.now())

    # step 4 kafka data load
    kafka_info = {
        "model_name": model_name,
        "userId": user_ids,
        "requestId": request_ids,
        "prompt": prompt,
        "stream": use_stream,
        "logprobs": return_log_probs,
        "badWordsIds": bad_words_ids,
        "stopWordsIds": stop_words_ids,
        "useRandom": request_json["useRandom"] if "useRandom" in request_json.keys() else True,
        "randomSeed": new_request_json["random_seed"][0][0],
        "runtimeTopK": new_request_json["runtime_top_k"][0][0],
        "runtimeTopP": new_request_json["runtime_top_p"][0][0],
        "beamWidth": new_request_json["beam_width"][0][0],
        "repetitionPenalty": new_request_json["repetition_penalty"][0][0],
        "lenPenalty": new_request_json["len_penalty"][0][0],
        "temperature": new_request_json["temperature"][0][0],
        "beamSearchDiversityRate": new_request_json["beam_search_diversity_rate"][0][0],
        "startId": llama_triton_client.start_id,
        "endId": llama_triton_client.end_id,
        "requestOutputLen": new_request_json["request_output_len"][0][0],
        "inputLengths": new_request_json["input_lengths"][0][0],
        "inputIds": str(new_request_json["input_ids"][0].tolist()),
        "badWordsList": str(new_request_json["bad_words_list"][0].tolist()),
        "stopWordsList": str(new_request_json["stop_words_list"][0].tolist()),
        "text": re_data["result"]["text"] if "result" in re_data.keys() and "text" in re_data["result"].keys() else "",
        "index": re_data["result"]["index"] if "result" in re_data.keys() and "index" in re_data["result"].keys() else -1,
        "promptTokens": re_data["usage"]["promptTokens"] if "usage" in re_data.keys() and "promptTokens" in re_data["usage"].keys() else new_request_json["input_lengths"][0][0],
        "completionTokens": re_data["usage"]["completionTokens"] if "usage" in re_data.keys() and "completionTokens" in re_data["usage"].keys() else 0,
        "totalTokens": re_data["usage"]["totalTokens"] if "usage" in re_data.keys() and "totalTokens" in re_data["usage"].keys() else new_request_json["input_lengths"][0][0],
        "finish": re_data["finish"] if "finish" in re_data.keys() else False,
        "success": True
    }
    if evn == "online": logger.info(f"[kafka log]: {log_prefix}kafka_info data={kafka_info}")
    logger.info(f"{log_prefix}triton_client.run close")
    del result_queue
    # print("main_logic kafka push: ", datetime.datetime.now())


if __name__ == "__main__":
    workers = workers_num  # 进程数
    app.run(host="0.0.0.0", port=port, workers=workers, debug=False)




