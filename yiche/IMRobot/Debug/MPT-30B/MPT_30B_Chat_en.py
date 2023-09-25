# -*- coding: utf-8 -*-

from websocket import create_connection
import requests
import json
import time

# with open("./case_20230620_wj+wd.json", "r", encoding='UTF-8') as f:
#     data = json.load(f)
#     for i in data:
#         with open(f"./en_input.txt", "a", encoding="utf-8") as inp:
#             inp.write("""Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:
#
# Vehicle parameter configuration: You just know vehicle parameter, eg: price, power, fuel, noise, internal configuration, space, comfort, color, vehicle manufacturer and other information, Action Input is the vehicle name value in conversation history and vehicle parameter.
# Vehicle reviews: check the advantages and disadvantages of vehicles, reviews, driving experience.
# Vehicle FAQ query: query answers based on user questions, recommend popular brands and models of vehicles, input is user questions.
# Vehicle brand and series recognition: If '根据用户图片内容' not in 'Question: ', you absolutely not be able to use this tool.You can identify the brand and model of the vehicle in the picture, the input should be the user's picture.
# Image content recognition: recognition and understand image content
#
# Use the following format:
#
# Question: the input question you must answer
# Thought: you should always think about what to do
# Action: the action to take, should be one of [Vehicle FAQ query, Vehicle parameter configuration, Vehicle reviews, Vehicle brand and series recognition, Image content recognition]
# Action Input: the input to the action
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can repeat N times)
# Thought: 我现在知道最终答案
# Final Answer: 返回Observation的内容作为最终答案
#
# Please note:
#
# If you already know the answer to the question, be sure to output "Final Answer: Answer to the question" immediately.
# 如果"User:"中"图片内容"识别为"汽车", 务必选择"Vehicle Brand and Series Recognition"工具来确定车型车系.
#
# Begin! Remember to speak as a pirate when giving your final answer. Use lots of "Arg"s
#
# Conversation history:\n""")
#             if len(i["history"]) > 0:
#                 for y in i["history"]:
#                     inp.write(f'User:{y["user"]}\nAgent:{y["agent"]}\n')
#                 inp.write(f'\nQuestion:{i["question"]}\n')
#                 inp.write("Thought：\n")
#                 inp.write('-' * 100 + '\n')
#             else:
#                 inp.write(f'\nQuestion:{i["question"]}\n')
#                 inp.write("Thought：\n")
#                 inp.write('-' * 100 + '\n')

start_time = time.time()
result_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
with open(f"./en_input.txt", "r", encoding="utf-8") as f:
    datas = f.read().split('-'*100 + '\n')
    datas.pop()
    for i in datas:
        url = "https://mosaicml-mpt-30b-chat.hf.space/run/predict"
        header = {"Content-Type": "application/json"}
        data = {"data": [f'{i}', []], "event_data": None, "fn_index": 2, "session_hash": "e2xbnyj984"}
        res = requests.post(url=url, data=json.dumps(data), headers=header)
        ws_url = 'wss://mosaicml-mpt-30b-chat.hf.space/queue/join'
        ws = create_connection(ws_url)
        ws.send('{"fn_index":2,"session_hash":"e2xbnyj984"}')
        ws_data = {"data": ["", [[f'{i}', ""]]], "event_data": None, "fn_index": 3, "session_hash": "e2xbnyj984"}
        ws.send(json.dumps(ws_data))
        result = ws.recv()
        while json.loads(result)["msg"] != "process_completed":
            result = ws.recv()
            if json.loads(result)["msg"] == "process_completed":
                print(f'返回结果为：{json.loads(result)}')
                print(f'输入为：\n{json.loads(result)["output"]["data"][1][0][0]}')
                print("-"*50)
                print(f'结果为：\n{json.loads(result)["output"]["data"][1][0][1]}')
                print("-" * 100)
                with open(f"./en_result_{result_time}.txt", 'a', encoding="utf-8") as ff:
                    ff.write(f'prompt：\n{json.loads(result)["output"]["data"][1][0][0]}\n')
                    ff.write("-"*50 + '\n')
                    ff.write(f'result：\n{json.loads(result)["output"]["data"][1][0][1]}\n')
                    ff.write("-" * 100 + '\n')
end_time = time.time()
finish_time = end_time - start_time
print(f'测试完成时间为%.2f分钟' % (finish_time / 60))



