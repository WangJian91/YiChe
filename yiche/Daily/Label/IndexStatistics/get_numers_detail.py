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

args = sys.argv

with open(args[1], 'r') as fcc_file:
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
        asr_label = ""
        if('asr_label' in label_dict):
            asr_label= label_dict['asr_label']

        print(str(convid)+"\t"+str(iterm['id'])+"\t"+str(label_msg)+"\t"+str(intent)+"\t"+str(label_dict['source-Label'])+"\t"+str(label_dict['asr'])+"\t"+asr_label+"\t"+str(nlu_flag)+"\t"+str(label_dict['nlu'])+"\t"+str(label_dict['break'])+"\t"+str(label_dict['noise']))
