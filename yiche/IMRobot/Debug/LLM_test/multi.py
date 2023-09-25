# -*- coding: utf-8 -*-
import asyncio
import time
import websockets
import queue
import json
from multiprocessing import Process


async def send_msg(websocket, prompt, r_queue):
    input_data = {
        "appId": "d3dfea3f-16d3-47b0-b1ca-2fee8e6ecd7c",  # llama
        # "appId": "5923bf20-4771-422e-9f76-9b8f0b9317c5",  # chatglm
        # "appId": "09105f2b-cd2b-45f9-8dc6-7800f262c0f8",   #aquila
        # "appId": "5e2c8b7c-d3f6-4895-986a-26cefdc4f8e6",   #ziya
        "version": "vicuna-13b",  # 如果没有找到会用默认的
        "userId": "IN0001",  # 找算法工程组获取
        "userRequestId": "222",
        "requestId": "1111",
        "maxTokens": 138,
        "stream": True,
        #"stream": False,
        "useRandom": False,
        "prompt": prompt,
        # "img": base64.b64encode(img_file).decode(),
        # "topK": 1,
        # "topP": 1,
        "temperature": 0.1,
        "repetitionPenalty": 1,
        # "stopWordsIds": [[6039, 2140, 362], [13, 16492]],
        # "stopWords": ["输出"],
        # "badWordsIds": [[362]],
        "extra": {"rrrr": 666}
    }
    await websocket.send(json.dumps(input_data))
    recv_data = prompt
    # print(prompt)
    while True:
        print(prompt)
        recv_text = await websocket.recv()
        recv_json = json.loads(recv_text)
        if recv_json and "data" in recv_json and "result" in recv_json["data"] and "text" in recv_json["data"][
            "result"]:
            recv_data = recv_json["result"]["text"]
        if recv_json["finish"]:
            print(recv_json)
            break
        print(recv_json)


async def main_logic(prompt, r_queue):
    async with websockets.connect('ws://127.0.0.1:17862/llm/ft_vicuna_16k', ping_timeout=10000) as websocket:
        # async with websockets.connect('ws://127.0.0.1:8080/',ping_timeout=10000) as websocket:

        # t = time.time()
        # print(t)
        await send_msg(websocket, prompt, r_queue)
        # print(time.time() - t)


# def run():
def run(prompt):
    # prompt = "北京著名景点"
    r_queue = queue.Queue()
    t = time.time()
    asyncio.run(main_logic(prompt, r_queue))
    print(time.time() - t)


size = 1
text_list = ["北京著名景点", "You are a Language Retelling Engineer."] * size
for i in range(size):
    p = Process(target=run, kwargs={"prompt": text_list[i] + str(i)})
    # t = threading.Thread(target=run, args=(text_list[i],))
    #t.start()
    p.start()


