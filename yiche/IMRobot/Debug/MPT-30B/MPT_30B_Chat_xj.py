# -*- coding: utf-8 -*-

from websocket import create_connection
import requests
import json
import time

json_file = "./0711.json"
input_file = "./xj_input.txt"
# with open(json_file, "r", encoding='UTF-8') as f:
#     data = json.load(f)
#     for i in data:
#         with open(input_file, "a", encoding="utf-8") as inp:
#             history_str = ''
#             question_str = ''
#             if len(i["history"]) > 0:
#                 for y in i["history"]:
#                     if 'agent' not in y:
#                         history_str += f'User:{y["user"]}'
#                     else:
#                         history_str += f'User:{y["user"]}\nAgent: {y["agent"]}\n'
#                 question_str += f'{i["question"]}'
#             else:
#                 question_str += f'{i["question"]}'
#             inp.write(f"""You are a Language Retelling Engineer. Answer the following questions as best you can.
# First you need to analyze the conversation history.
# Extract dialogue logic and entity information that appears in the conversation history.
#
# Then you need to complete the user question information based on the user question.
# During the retelling generate, you can complete the following types of natural language processing tasks:
# eg: Chinese referential disambiguation tasks, complete dialogue discuss vehicle series in Retelling etc.
#
# <example>
# ```
# Conversation history = [
# User: 这款车的口碑怎样,
# Agent: 根据已知信息，天籁这款车的口碑较好，消费者对其动力、操控、舒适性和空间等方面评价较高。但也有一些消费者对其外观和内饰提出了质疑。总体来说，天籁是一款性价比较高的中型车，值得消费者考虑。",
# User: 售价多少,
# Agent: 根据已知信息，天籁目前在售车型有2.0l和2.0t两款发动机可供选择，售价从17.98万元到26.98万元不等，目前厂家指导价优惠3万元左右，可以参考一下这个价格。因此，天籁",
# User: 变速箱怎样,
# Agent: 天籁的工程师可能会告诉你，天籁使用的cvt变速箱表现很不错，具有平顺性、油耗和扭矩控制等优点。但是，cvt变速箱不太适合大排量发动机，因此可能无法提供与大排量发动机相匹配的驾驶体验。"
# ]
# ```
# User Question: '容易坏吗'
# User Retelling Question: 天籁质量怎么样？容易坏吗？
# </example>
#
# Note: Ensure generated retelling to use the user's perspective and personal name.
# Note: Please provide the generate in Chinese.
#
# Now let's start retelling:
# Conversation history = [
# {history_str}
# ]
# User Question: '{question_str}'
# Thought: you should always think about what to do
# User Retelling Question: \n""")
#             inp.write('-' * 100 + '\n')

start_time = time.time()
result_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
with open(input_file, "r", encoding="utf-8") as f:
    datas = f.read().split('-'*100 + '\n')
    datas.pop()
    print(len(datas))
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
                with open(f"./zh_result_{result_time}.txt", 'a', encoding="utf-8") as ff:
                    ff.write(f'prompt：\n{json.loads(result)["output"]["data"][1][0][0]}\n')
                    ff.write("-"*50 + '\n')
                    ff.write(f'result：\n{json.loads(result)["output"]["data"][1][0][1]}\n')
                    ff.write("-"*100 + '\n')
end_time = time.time()
finish_time = end_time - start_time
print(f'测试完成时间为%.2f分钟' % (finish_time / 60))
