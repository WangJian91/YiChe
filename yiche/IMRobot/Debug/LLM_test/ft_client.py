# -*- coding: utf-8 -*-
import asyncio
import time
import websockets
import queue
import json


async def send_msg(websocket, prompt, r_queue):
        input_data = {
                'maxTokens': 39,
                "userId": "IN0001",
                "requestId": "1111",
                'prompt': prompt,
                'repetitionPenalty': 1,
                'stream': False,
                'temperature': 0.1,
                'useRandom': False
        }
        await websocket.send(json.dumps(input_data))
        while True:
            recv_text = await websocket.recv()
            recv_json = json.loads(recv_text)
            if recv_json and "data" in recv_json and "result" in recv_json["data"] and "text" in recv_json["data"]["result"]:
                recv_data = recv_json["result"]["text"]
            if recv_json["finish"]:
                print(recv_json)
                break
            print(recv_json)


async def main_logic(prompt, r_queue):
    # async with websockets.connect('ws://127.0.0.1:17862/') as websocket:
    async with websockets.connect('ws://aiplatform-gn.inneryiche.com/llm/ft_vicuna_16k') as websocket:
        await send_msg(websocket, prompt, r_queue)

prompt = "北京著名景点"


r_queue = queue.Queue()
t = time.time()
asyncio.run(main_logic(prompt, r_queue))
print(time.time() - t)

