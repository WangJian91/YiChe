# -*- coding: utf-8 -*-
import json

# num_list = [129889, 130113, 130108, 130105, 129843]
# with open('./qa.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     for d in data:
#         if len(d['annotations'][0]['result']) != len(d['data']['info']['Unnamed: 0']):
#             if d['id'] not in num_list:
#                 print(d['id'], '存在漏标项')


num_list = [217161, 217145]
with open('./qa1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for d in data:
        try:
            if len(d['annotations'][0]['result'][0]['value']['choices']) < 1:
                print(d['id'], '漏标')
        except IndexError:
            if d['id'] not in num_list:
                print(d['id'], '漏标')



