# -*- coding: utf-8 -*-
import time
import threading
from websocket import create_connection
import json


def send_msg(prompt):
    url = 'ws://127.0.0.1:17862/'
    ws = create_connection(url)
    input_data = {
        "appId": "d3dfea3f-16d3-47b0-b1ca-2fee8e6ecd7c",  # llama
        # "appId": "5923bf20-4771-422e-9f76-9b8f0b9317c5",  # chatglm
        # "appId": "09105f2b-cd2b-45f9-8dc6-7800f262c0f8",   #aquila
        # "appId": "5e2c8b7c-d3f6-4895-986a-26cefdc4f8e6",   #ziya
        "version": "vicuna-13b",  # 如果没有找到会用默认的
        "userId": "IN0001",  # 找算法工程组获取
        "userRequestId": "222",
        "requestId": "1111",
        "maxTokens": 38,
        "stream": True,
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
    t = time.time()
    # print('----------', t)
    ws.send(json.dumps(input_data))
    print('----------', t)
    while True:
        recv_text = ws.recv()
        recv_json = json.loads(recv_text)
        if recv_json and "data" in recv_json and "result" in recv_json["data"] and "text" in recv_json["data"]["result"]:
            recv_data = recv_json["result"]["text"]
        if recv_json["finish"]:
            print(recv_json)
            break
        print(recv_json)
    print(time.time() - t)


prompt_list = ["You are a Language Retelling Engineer", "北京的景区"]
size = 2
for i in range(size):
    t = threading.Thread(target=send_msg, args=(i,))
    t.start()




