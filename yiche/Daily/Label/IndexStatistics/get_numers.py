# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import time
import requests
import urllib
import sys
import json
import uuid

args = './0504/data.json'
with open(args, 'r', encoding='utf-8') as fcc_file:
# with open('C:\Users\wb_wangjian\Desktop\Label\IndexStatistics\0504\project-167-at-2023-05-04-08-49-854ca961.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    for iterm in fcc_data:
        annotations = iterm['annotations']
        results = annotations[0]['result']
        audio = iterm['data']['audio']
        convid = audio.strip().split("/")[-2]
        convd_msg = iterm['data']['convd']
        convd_msg_ls = convd_msg.strip().splitlines()
        label_msg = convd_msg_ls[0].strip().split(':')[1]
        intent = ""
        for msg in convd_msg_ls:
            if msg.find('intent') > -1:
                mms = msg.strip().split("    ")[0].strip().split(":")[1]
                if mms == label_msg:
                    intent = msg.strip().split('intent:')[-1]
        label_dict = dict()
        for res in results:
            #print(res['from_name'],res['value'])
            if(res['from_name'] == 'transcription'):
                label_dict['asr_label'] = res['value']['text'][0]
            elif(res['from_name'] == 'nlu'):
                label_dict[res['from_name']] = res['value']['choices']

            else:
                label_dict[res['from_name']] = res['value']['choices'][0]
        nlu_flag = 0
        if(intent in label_dict['nlu']): 
            nlu_flag = 1
        print(str(convid)+"\t"+str(iterm['id'])+"\t"+str(label_msg)+"\t"+str(intent)+"\t"+str(label_dict['source-Label'])+"\t"+str(label_dict['asr'])+"\t"+str(nlu_flag)+"\t"+str(label_dict['break'])+"\t"+str(label_dict['noise']))
