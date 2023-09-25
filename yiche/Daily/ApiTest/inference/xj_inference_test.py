import asyncio
import datetime
import time
import websockets
import queue
import json

# type = 1
# url = "ws://aiplatform-gn.inneryiche.com/llm/ft_vicuna_16k"
# type = 2
# url = 'ws://aiplatform-gn-uat.inneryiche.com/arges/taskflow/infer/ws'
type = 2
url = 'ws://aiplatform-pbs.inneryiche.com/arges/taskflow/infer/ws'
# type = 1
# url = "ws://aiplatform-gn.inneryiche.com/llm/ft_vicuna_16k"


async def send_msg(websocket, prompt):
    if type == 1:
        input_data = {
            "userId": "IN0001",
            "requestId": "1111",
            'maxTokens': 128,
            'prompt': prompt,
            'repetitionPenalty': 1,
            'stream': True,
            'temperature': 0.1,
            'useRandom': False
        }
    else:
        input_data = {
            "appId": "d3dfea3f-16d3-47b0-b1ca-2fee8e6ecd7c",  # llama
            "version": "vicuna-13b-v1.5-16k",  # 如果没有找到会用默认的
            "userId": "IN0001",
            "userRequestId": "222",
            "requestId": "1111",
            "data": {
                "userId": "IN0001",
                "requestId": "1111",
                "stream": True,
                "useRandom": False,
                "maxTokens": 128,
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
        # print(recv_json)
        if type == 1: recv_data = recv_json["result"]["text"]
        else: recv_data = recv_json["data"]["result"]["text"]
        if (type == 1 and recv_json["finish"]) or (type == 2 and recv_json["data"]["finish"]):
            print(recv_data)
            break
        print(recv_data)


async def main_logic(prompt):
    async with websockets.connect(url, ping_timeout=1000) as websocket:
        t = time.time()
        await send_msg(websocket, prompt)
        print(time.time() - t)


asyncio.run(main_logic("北京著名景点"))