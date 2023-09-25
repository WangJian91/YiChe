# -*- coding: utf-8 -*-
import asyncio
import datetime
import time
import websockets
import json


async def send_msg(websocket, prompt, max_tokens):
    input_data = {
        "appId": "642279f5-a6ef-479c-bb5a-0432dce3ac46",  # baichuan13b
        "version": "baichuan2-13b-chat",  # 如果没有找到会用默认的
        "userId": "IN0001",
        "userRequestId": "222",
        "requestId": "1111",
        "data": {
            "userId": "IN0001",
            "requestId": "1111",
            "stream": True,
            "useRandom": False,
            "maxTokens": max_tokens,
            "prompt": prompt,
            "temperature": 0.1,
            "repetitionPenalty": 1.0,
        },
        "extra": {"rrrr": 666}
    }
    await websocket.send(json.dumps(input_data))
    while True:
        recv_text = await websocket.recv()
        recv_json = json.loads(recv_text)
        if recv_json and "data" in recv_json and "result" in recv_json["data"] and "text" in recv_json["data"]["result"]:
            context = recv_json["data"]["result"]["text"].replace('\n', '')
            if len(context) > 0:
                print(context)
            if recv_json["data"]["finish"]:
                print(recv_text)
                promptTokens = recv_json["data"]["usage"]["promptTokens"]
                completionTokens = recv_json["data"]["usage"]["completionTokens"]
                print("prompt长度:", promptTokens)
                print("返回文本长度:", completionTokens)
                break
        else:
            print(recv_text)


async def main_logic(url, prompt, max_tokens):
    async with websockets.connect(url) as websocket:
        t = time.time()
        await send_msg(websocket, prompt, max_tokens)
        print(time.time() - t)

if __name__ == '__main__':
    # url = 'ws://aiplatform-gn-uat.inneryiche.com/arges/taskflow/infer/ws'
    url = 'ws://aiplatform-pbs.inneryiche.com/arges/taskflow/infer/ws'
    # prompt = "请介绍下北京吧: "
    # prompt = "北京著名景点有"
    # prompt = "You are a Language Retelling Engineer.Please retell some interesting things. begin"
    prompt = "你是一个资深劳动合同拟定师，需要尽可能详细的拟定一份4520字的劳动合同，其中需要2000字的劳动仲裁法，2000多字的公司职工保护义务法"
    # max_tokens = 200
    max_tokens = 1000
    asyncio.run(main_logic(url, prompt, max_tokens))
