# -*- coding: utf-8 -*-

from IMRobot.Common.logger_util import error_log, logs
from IMRobot.Common.parameterize_util import *
from websocket import create_connection
import json
import websockets
import re
import traceback
import jieba
import asyncio
import time


class RequestsUtil:

    def __init__(self, obj):
        self.obj = obj

    def parse_llm_output(self, llm_output: str):

        action = json.loads(llm_output)['data']['result']['text'].split('Action: ')[1].split('\n')[0]
        action_input = json.loads(llm_output)['data']['result']['text'].split('Action Input: ')[1].split('\n')[0]
        return action, action_input

    def send_msg(self, case_info):
        history = case_info['history']
        question = case_info['question']
        self.action_label = case_info['action_label']
        self.action_input_info = case_info['action_input_info']
        template_en = f"""Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:

                    Vehicle parameter configuration: You just know vehicle parameter, eg: price, power, fuel, noise, internal configuration, space, comfort, color, vehicle manufacturer and other information, Action Input is the vehicle name value in conversation history and vehicle parameter.
                    Vehicle reviews and FAQ query: check the advantages and disadvantages of vehicles, reviews, driving experience, answer common questions about cars, recommend popular brands and models of vehicles.
                    Vehicle brand and series recognition: If '根据用户图片内容' not in 'Question: ', you absolutely not be able to use this tool.You can identify the brand and model of the vehicle in the picture, the input should be the user's picture.
                    Image content recognition: recognition and understand image content

                    Use the following format:

                    Question: the input question you must answer
                    Thought: you should always think about what to do
                    Action: the action to take, should be one of [Vehicle parameter configuration, Vehicle reviews and FAQ query, Vehicle brand and series recognition, Image content recognition]
                    Action Input: the input to the action, including all car series and brand names extracted from the conversation history.
                    Observation: the result of the action
                    ... (this Thought/Action/Action Input/Observation can repeat N times)
                    Thought: 我现在知道最终答案
                    Final Answer: 返回Observation的内容作为最终答案

                    Please note:

                    If you already know the answer to the question, be sure to output "Final Answer: Answer to the question" immediately.
                    如果"User:"中"图片内容"识别为"汽车", 务必选择"Vehicle Brand and Series Recognition"工具来确定车型车系.

                    Begin! Remember to speak as a pirate when giving your final answer. Use lots of "Arg"s

                    Conversation history:
                    {history}

                    Question: {question}
                    Thought:"""

        input_data = {
            "appId": "d3dfea3f-16d3-47b0-b1ca-2fee8e6ecd7c",  # llama
            "version": "vicuna-13b",  # 如果没有找到会用默认的
            "userId": "OT0006",
            "userRequestId": "222",
            "requestId": "1111",
            "data": {
                "stream": False,
                # "logprobs": 5,
                "useRandom": False,
                "prompt": template_en,
                "topK": 1,
                "maxTokens": 2048,
                "stopWords": ["Observation", "Question"],
                "stopWordsIds": [[6039, 2140, 362], [13, 16492]],
            },
            "extra": {"rrrr": 666}
        }
        base_url = read_config("base", "ws_url")
        logs("--------测试开始--------")
        logs("question：%s" % question)
        logs("action_label：%s" % self.action_label)
        logs("action_input_info：%s" % self.action_input_info)
        # async with create_connection(base_url) as websocket:
        # with websockets.connect(base_url, ping_timeout=1000) as websocket:
        start_time = time.time()
        websocket = create_connection(base_url, ping_timeout=1000)
        websocket.send(json.dumps(input_data))
        result = websocket.recv()
        print(time.time() - start_time)
        return result

    def assert_func(self, result_text):

        zh_en_mapping = {
            "车辆参配查询": "Vehicle parameter configuration",
            "汽车点评和常见问题查询": "Vehicle reviews and FAQ query",
            "车辆品牌车型识别": "Vehicle brand and series recognition",
            "图片内容识别": "Image content recognition",
        }
        flag = 0
        print(result_text)
        logs(result_text)
        action, action_result = self.parse_llm_output(result_text)
        action_label_en = zh_en_mapping[self.action_label]
        if action_label_en in action:
            flag += 1
            logs(f'action_label_en:{action_label_en}')
            logs(f'action_result:{action}')
            logs("断言成功")
            logs("--------测试结束--------\n")
        else:
            logs(f'action_label_en:{zh_en_mapping[self.action_label]}')
            logs(f'action_result:{action}')
            logs("断言失败")
            logs("--------测试结束--------\n")
        assert flag == 1

    # 规范YAML测试用例
    def standard_yaml(self, case_info):
        case_info_key = case_info.keys()
        if "history" in case_info_key and "question" in case_info_key and "action_label" in case_info_key\
                and "action_input_info" in case_info_key:
            result_text = self.send_msg(case_info)
            self.assert_func(result_text)
        else:
            error_log('测试用例格式错误')


if __name__ == '__main__':
    pass
