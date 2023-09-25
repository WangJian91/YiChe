# -*- coding: utf-8 -*-
import asyncio
import time
import datetime
import os
from websocket import create_connection
import json
import traceback
import logging
from builtins import Exception


file_log_level = 'info'
console_log_level = 'info'


def create_log(logger_name='log'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        file_log_path = os.getcwd() + "/Logs/" + str(datetime.date.today()) + ".log"
        # file_log_path = os.getcwd() + "/Logs/log.log"
        if not os.path.isdir(os.getcwd() + "/Logs/"):
            os.mkdir(os.getcwd() + "/Logs/")
        file_handler = logging.FileHandler(file_log_path, encoding='utf-8')
        if file_log_level == "info":
            file_handler.setLevel(logging.INFO)
        elif file_log_level == "error":
            file_handler.setLevel(logging.ERROR)

        # 4.创建文件日志格式
        file_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s'))
        # 将文件日志的控制器加入到日志对象
        logger.addHandler(file_handler)
        # -------控制台日志----------
        # 1.创建控制台日志的控制器
        console_handler = logging.StreamHandler()
        # 2.创建控制台日志的日志级别
        if console_log_level == "info":
            console_handler.setLevel(logging.INFO)
        elif console_log_level == "error":
            console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s'))
        logger.addHandler(console_handler)
    return logger


def send_msg(url, maxtokens):
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
    ws = create_connection(url)
    ws.send(json.dumps(input_data))
    t = time.time()
    while True:
        recv_text = ws.recv()
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
    print(time.time() - t)
    return recv_text


if __name__ == '__main__':
    url = 'ws://aiplatform-pbs.inneryiche.com/arges/taskflow/infer/ws1'
    # url = 'ws://aiplatform-gn.inneryiche.com/llm/ft_vicuna_16k'
    # # url = 'ws://aiplatform-gn-uat.inneryiche.com/arges/taskflow/infer/ws'
    # url = 'ws://aiplatform-gn-uat.inneryiche.com/llm/ft_vicuna_16k'
    # url = 'ws://aiplatform-gn-test.yiche.com/arges/taskflow/infer/ws'
    # prompt = "北京著名景点有"
    # prompt = "北京有那些著名景点"
    # prompt = "宝马是"
    prompt = "你是一个资深法律制定者，需要尽可能详细的写一个超过4555字的法律文献，有关劳动法的细则"
    # prompt = "  "
    # prompt = ""
    max_tokens = 1064
    # send_msg(url, max_tokens)
    while True:
        try:
            result = send_msg(url, max_tokens)
            time.sleep(2)
            create_log().info(result)
        except Exception as e:
            create_log().error(traceback.format_exc())
            time.sleep(60)

