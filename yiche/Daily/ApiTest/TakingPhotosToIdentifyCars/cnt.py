# -*- coding: utf-8 -*-
import json

# 全部识别失败，且分数大于0.3
# with open('./identify_result.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     a = 0
#     for i in data:
#         if i != 'analysis':
#             for y in data[i]:
#                 if isinstance(data[i][y], list):
#                     if data[i][y][-1] == '全部识别失败' and data[i][y][0]['top1']['score'] >= 0.3:
#                         a += 1
#                         print(y, ':', data[i][y])
#     print(a)


# 识别错误的照片方位
orientations = {
    "前": 0,
    "后": 0,
    "左侧": 0,
    "右侧": 0,
    "左前": 0,
    "右前": 0,
    "左后": 0,
    "右后": 0
}
with open('./identify_result.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for i in data:
        if i != 'analysis':
            for y in data[i]:
                if isinstance(data[i][y], list):
                    if data[i][y][-1] == '全部识别失败':
                        a = y.replace('.jpg', '')
                        if a.endswith('左'):
                            print(a)
                        orientation = y.replace('.jpg', '').replace(i, '').replace('1', '').replace('.png', '')
                        orientations[orientation] += 1
print(orientations)

