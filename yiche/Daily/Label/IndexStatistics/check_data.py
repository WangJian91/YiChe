# -*- coding: utf-8 -*-
import json

args = './0504/data.json'
with open(args, 'r', encoding='utf-8') as fcc_file:
    fcc_data = json.load(fcc_file)
    for iterm in fcc_data:
        # print(iterm)
        iterm['data']['convd'] = ''
        if 'ASR' not in str(iterm):
            print('未标注ASR:', iterm)
        if '被打断' not in str(iterm):
            print('未标注全双工:', iterm)
        if '意图' not in str(iterm):
            if '其他' not in str(iterm):
                print('未标注意图:', iterm)
        if '噪音' not in str(iterm):
            print('未标注噪音:', iterm)
        if '用户挂断' not in str(iterm):
            if '系统挂断' not in str(iterm):
                print('未标注线索:', iterm)
        if '成功' not in str(iterm):
            if '失败' not in str(iterm):
                print('未标注成功单:', iterm)
