# -*- coding: utf-8 -*-

import json

# # 标注数据格式转换
# with open('./data3.json', 'r', encoding='UTF-8') as f:
#     data = json.load(f)
#     # print(data)
#     with open('./form3.json', 'w', encoding='UTF-8') as ff:
#         json.dump(data, ff, ensure_ascii=False, indent=4)


# 标注数据漏标项检查
with open('./data5.json', 'r', encoding='utf-8') as f:
    num_list = [197964, 193059, 193060, 198468, 198437, 200584, 195457, 201383]
    data = json.load(f)
    for d in data:
        result = d['annotations'][0]['result']
        task_id = d['id']
        if len(result) < 3:
            if len(result) == 0:
                print(f'{task_id}:未标注')
            else:
                result_list = []
                for r in result:
                    result_list.append(r['from_name'])
                    if r['from_name'] == '_action':
                        choices = r['value']['choices']
                        if '闲聊' in choices or '无效' in choices or '骂人' in choices or '其他' in choices:
                            if len(result) > 1:
                                if task_id not in num_list:
                                    print(task_id, '存在多余标注项')
                        else:
                            if task_id not in num_list:
                                print(task_id, '存在漏标项')
                if '_action' not in result_list:
                    if task_id not in num_list:
                        print(task_id, 'action未标注')
        else:
            result_list = []
            for r in result:
                result_list.append(r['from_name'])
                if r['from_name'] == '_action':
                    choices = r['value']['choices']
                    if '闲聊' in choices or '无效' in choices or '骂人' in choices or '其他' in choices:
                        if len(result) > 1:
                            if task_id not in num_list:
                                print(task_id, '存在多余标注项')


# with open('./data1.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     for d in data:
#         result = d["annotations"][0]["result"]
#         for i in result:
#             if i["from_name"] == '_action':
#                 if i["value"]["choices"][0] == '汽车常见问题查询':
#                     print(d["id"], ':', d["data"]["humanMachineDialogue"][-2])


