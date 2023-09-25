# -*- coding: utf-8 -*-
import asyncio
import time
import websockets
import json


async def send_msg(websocket, input_data):
    await websocket.send(json.dumps(input_data))
    while True:
        recv_text = await websocket.recv()
        # print(recv_text)
        recv_json = json.loads(recv_text)
        if 'pbs' in url or 'gn-test' in url and recv_json["code"] == 0:
            if recv_json["data"]["finish"]:
                # print(recv_json)
                context = recv_json["data"]["result"]["text"].replace('\n', '')
                promptTokens = recv_json["data"]["usage"]["promptTokens"]
                completionTokens = recv_json["data"]["usage"]["completionTokens"]
                print(context)
                print("prompt长度:", promptTokens)
                print("返回文本长度:", completionTokens)
                break
            context = recv_json["data"]["result"]["text"].replace('\n', '')
            if len(context) > 0:
                print(context)

        elif 'gn.inneryiche' in url or "gn-uat" in url and recv_json["code"] == 0:
            recv_data = recv_json["result"]["text"].replace('\n', '')
            if recv_json["finish"]:
                print(recv_data)
                promptTokens = recv_json["usage"]["promptTokens"]
                completionTokens = recv_json["usage"]["completionTokens"]
                print("prompt长度:", promptTokens)
                print("返回文本长度:", completionTokens)
                break
            if len(recv_data) > 0:
                print(recv_data)
        else:
            print(recv_text)


async def main_logic(prompt, maxtokens, url):
    input_data = dict()
    if 'pbs' in url or 'gn-test' in url:
        input_data = {
            "appId": "d3dfea3f-16d3-47b0-b1ca-2fee8e6ecd7c",
            "version": "vicuna-13b-v1.5-16k",
            "userRequestId": "222",
            "data": {
                "requestId": "1111",
                "userId": "IN0001",
                "maxTokens": maxtokens,
                "stream": True,
                # "stream": False,
                "useRandom": False,
                "prompt": prompt,
                "temperature": 0.1,
                "repetitionPenalty": 1
            },
            "extra": {"rrrr": 666}
        }
    elif 'gn.inneryiche' in url or "gn-uat" in url:
        input_data = {
            "userId": "IN0001",
            "requestId": "1111",
            'maxTokens': maxtokens,
            'prompt': prompt,
            'repetitionPenalty': 1,
            'stream': True,
            'temperature': 0.1,
            'useRandom': False
        }
    async with websockets.connect(url, ping_timeout=10000) as websocket:
        t = time.time()
        await send_msg(websocket, input_data)
        print(time.time() - t)

url = 'ws://aiplatform-pbs.inneryiche.com/arges/taskflow/infer/ws'
# url = 'ws://aiplatform-gn.inneryiche.com/llm/ft_vicuna_16k'
# # url = 'ws://aiplatform-gn-uat.inneryiche.com/arges/taskflow/infer/ws'
# url = 'ws://aiplatform-gn-uat.inneryiche.com/llm/ft_vicuna_16k'
# url = 'ws://aiplatform-gn-test.yiche.com/arges/taskflow/infer/ws'
prompt = "北京著名景点有"
# prompt = "北京有那些著名景点"
# prompt = "宝马是"
# prompt = "你是一个资深法律制定者，需要尽可能详细的写一个超过4555字的法律文献，有关劳动法的细则"
# prompt = "  "
# prompt = ""
max_tokens = 200
asyncio.run(main_logic(prompt, max_tokens, url))


