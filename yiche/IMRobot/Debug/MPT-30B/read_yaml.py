# -*- coding: utf-8 -*-

import yaml
import json

# with open("./case_20230620_wj+wd.json", "r", encoding='UTF-8') as f:
#     data = json.load(f)
#     # print(data)
#     # print(len(data))
#     for i in data:
#         if len(i["history"]) > 0:
#             print("History:")
#             for y in i["history"]:
#                 print(f'\tUser:{y["user"]}\n\tAgent:{y["agent"]}')
#             print(f'Question:{i["question"]}')
#             print(f'Label:{i["label"]}')
#             print('-' * 100)
#         else:
#             print("History:")
#             print(f'Question:{i["question"]}')
#             print(f'Label:{i["label"]}')
#             print('-' * 100)

# # prompt_en
# with open("./case_20230620_wj+wd.json", "r", encoding='UTF-8') as f:
#     data = json.load(f)
#     # print(data)
#     # print(len(data))
#     for i in data:
#         print("""Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:
#
# Vehicle FAQ query: query answers based on user questions, recommend popular brands and models of vehicles, input is user questions.
# Vehicle parameter configuration: You just know vehicle parameter, eg: price, power, fuel, noise, internal configuration, space, comfort, color, vehicle manufacturer and other information, Action Input is the vehicle name value in conversation history and vehicle parameter.
# Vehicle reviews: check the advantages and disadvantages of vehicles, reviews, driving experience.
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
# Conversation history:""")
#         if len(i["history"]) > 0:
#             for y in i["history"]:
#                 print(f'User:{y["user"]}\nAgent:{y["agent"]}')
#             print('\n')
#             print(f'Question:{i["question"]}')
#             print("Thought：")
#             print('-' * 100)
#             print('\n')
#         else:
#             print('\n')
#             print(f'Question:{i["question"]}')
#             print("Thought：")
#             print('-' * 100)
#             print('\n')


# prompt_zh
# with open("./case_20230620_wj+wd.json", "r", encoding='UTF-8') as f:
#     data = json.load(f)
#     # print(data)
#     # print(len(data))
#     for i in data:
#         print("""按照给定的格式回答以下问题。你可以使用下面这些工具：
#
# 汽车常见问题查询: 根据用户问题查询答案，推荐热门品牌和车型的车辆，输入的是用户问题。
# 车辆参配查询: 该工具只能查询车辆参数，例如：价格、动力、燃油、噪音、内部配置、空间、舒适度、颜色、车辆生产厂商等信息，Action Input是对话历史中的车辆名称值和车辆参数。
# 车辆点评: 查询车辆优缺点、点评、驾驶体验
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
# Conversation history:""")
#         if len(i["history"]) > 0:
#             for y in i["history"]:
#                 print(f'User:{y["user"]}\nAgent:{y["agent"]}')
#             print('\n')
#             print(f'Question:{i["question"]}')
#             print("Thought：")
#             print('-' * 100)
#         else:
#             print(f'\nQuestion:{i["question"]}')
#             print("Thought：")
#             print('-' * 100)
# prompt_zh_write
# with open("./case_20230620_wj+wd.json", "r", encoding='UTF-8') as f:
#     data = json.load(f)
#     for i in data:
#         with open("./input.txt", "a", encoding="utf-8") as inp:
#             inp.write("""按照给定的格式回答以下问题。你可以使用下面这些工具：
#
# 汽车常见问题查询: 根据用户问题查询答案，推荐热门品牌和车型的车辆，输入的是用户问题。
# 车辆参配查询: 该工具只能查询车辆参数，例如：价格、动力、燃油、噪音、内部配置、空间、舒适度、颜色、车辆生产厂商等信息，Action Input是对话历史中的车辆名称值和车辆参数。
# 车辆点评: 查询车辆优缺点、点评、驾驶体验
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
#                 inp.write("Thought：\n")
#                 inp.write('-' * 100 + '\n')
#             else:
#                 inp.write(f'\nQuestion:{i["question"]}\n')
#                 inp.write("Thought：\n")
#                 inp.write('-' * 100 + '\n')


# with open("./case.yaml", "w") as f:
#     yaml.dump(data=data, stream=f, allow_unicode=True)

# with open("./case.yaml", "r") as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     print(data)


