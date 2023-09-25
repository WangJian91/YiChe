# -*- coding: utf-8 -*-

import time
import json
import base64
import os
import sys
from tqdm import tqdm
import Levenshtein
import pandas as pd
import numpy as np
from multiprocessing import Process
import openpyxl
import datetime
import asyncio
import logging

# for i in range(1,21):
#     if i % 2 ==1:
#         print(f"abcd{i}-test")
#     else:
#         print(f"dcba{i}-test")

# start_time = time.time()
# time.sleep(61)
# end_time = time.time()
# finish_time = end_time - start_time
# print('%.2f分钟' % (int(finish_time) / 60))
# print('%.2f分钟' % (803 / 60))
# result_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
# print(result_time)

# sent1 = "宝马6GT的配置"
# sent2 = "宝马6GT"
# edit_dis = Levenshtein.distance(sent1, sent2)
# print(edit_dis)

# with open('./test.json', 'r', encoding='UTF-8') as f:
#     data = json.load(f)
#     print(data)
#     with open('./form.json', 'w', encoding='UTF-8') as ff:
#         json.dump(data, ff, ensure_ascii=False, indent=4)

# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
# print(time.strftime("%Y-%m-%d %H:%M:%S"))




