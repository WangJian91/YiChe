# -*- coding: utf-8 -*-

from websocket import create_connection
import requests
import json
import time

# with open("./case_20230620_wj+wd.json", "r", encoding='UTF-8') as f:
#     data = json.load(f)
#     for i in data:
#         with open(f"./zh_input.txt", "a", encoding="utf-8") as inp:
#             inp.write("""按照给定的格式回答以下问题。你可以使用下面这些工具：
#
# 车辆参配查询: 该工具只能查询车辆参数，例如：价格、动力、燃油、噪音、内部配置、空间、舒适度、颜色、车辆生产厂商等信息，Action Input是对话历史中的车辆名称值和车辆参数。
# 车辆点评: 查询车辆优缺点、点评、驾驶体验
# 汽车常见问题查询: 根据用户问题查询答案，推荐热门品牌和车型的车辆，输入的是用户问题。
# 车辆品牌车型识别: 如果'Question:'中没有'根据用户图片内容'，则绝对不能使用该工具。该工具可以识别图片中车辆的品牌和型号，输入的应该是用户的图片。
# 图片内容识别: 识别并理解图片内容
#
# 回答时需要遵循以下用---括起来的格式：
# ---
# Question: 我需要回答的问题
# Thought: 回答这个上述我需要做些什么
# Action: "汽车常见问题查询, 车辆参配查询, 车辆点评, 车辆品牌车型识别, 图片内容识别" 中的其中一个工具名
# Action Input: 选择工具所需要的输入
# Observation: 选择工具返回的结果
# ...（这个思考/行动/行动输入/观察可以重复N次）
# Thought: 我现在知道最终答案
# Final Answer: 原始输入问题的最终答案
# ---
#
# 请注意：
# ```
# 只回答客户问的问题，不要回复其他信息。
# ```
#
# 现在开始回答，记得在给出最终答案前多按照指定格式进行一步一步的推理。
#
# Conversation history:\n""")
#             if len(i["history"]) > 0:
#                 for y in i["history"]:
#                     inp.write(f'User:{y["user"]}\nAgent:{y["agent"]}\n')
#                 inp.write(f'\nQuestion:{i["question"]}\n')
#                 # inp.write(f'\nLabel:{i["label"]}\n')
#                 inp.write("Thought：\n")
#                 inp.write('-' * 100 + '\n')
#             else:
#                 inp.write(f'\nQuestion:{i["question"]}\n')
#                 # inp.write(f'\nLabel:{i["label"]}\n')
#                 inp.write("Thought：\n")
#                 inp.write('-' * 100 + '\n')

start_time = time.time()
result_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
with open(f"./zh_input.txt", "r", encoding="utf-8") as f:
    datas = f.read().split('-'*100 + '\n')
    datas.pop()
    print(len(datas))
    for i in datas:
        # print(i.split('Label:')[-1].split("\n")[0])
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
