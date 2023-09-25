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

args = './0506/log-2-21.txt'

with open(args, 'r', encoding='utf-8') as fcc_file:
    ls_all = []
    dialog_data = {}
    for line in fcc_file.readlines():
        ls_req_param = []
        if(line.find("DialogCore: param: {")>-1):
            trace_id = str(uuid.uuid1())
            datas= line.strip().split("DialogCore: param:")
            js = json.loads(datas[1].strip().replace("None", "\"\"").replace("\'", "\""))
            ls_req_param.append(str(js['sessionIdx']))
            ls_req_param.append(str(trace_id))
            ls_req_param.append(str(js['inParams']['tenantIdx']))
            ls_req_param.append(str(js['inParams']['robotIdx']))
            ls_req_param.append(str(js['inAction']))
            dialog_data[str(js['sessionIdx'])] = ls_req_param
        if(line.find("nlu result: time:")>-1):
            datas= line.strip().split("nlu result:")
            print(datas[-1])
            js = json.loads(datas[-1].replace("\'", "\"").replace("\"Confirm\": False",
                                                        "\"Confirm\": \"False\"").replace("\"Confirm\": True",
                                                        "\"Confirm\": \"True\"").replace("Idon\"t",
                                                        "Idont").replace("Idon\"", "Idon").replace("what\"syourname",
                                                        "whatsyourname").replace("嗯ohit\"","嗯ohit").replace("we\"LLtakeyouforaholidayandtime",
                                                        "weLLtakeyouforaholidayandtime").replace("I\"比亚迪","I比亚迪").
                                                        replace("that\"sa", "thatsa"))

            sid = datas[1].split(' ')[-2]
            dialog_data[sid].append(str(js['UserAction']))
            dialog_data[sid].append(str(js['Utter']))
            dialog_data[sid].append(str(js['Intents'][0]['IntentName']))
            dialog_data[sid].append(str(js['Intents'][0]['IntentIdx']))
            dialog_data[sid].append(str(js['Intents'][0]['IntentConf']))

        if(line.find("dm result:time:")>-1):
            datas= line.strip().split("dm result:")
            js = json.loads(datas[-1].replace("\'", "\"").replace("False","\"False\"").replace("True","\"True\""))
            sid = datas[1].split(' ')[-2]
            dialog_data[sid].append(str((js['ExecuteActionType'])))
            dialog_data[sid].append(str((js['Prompt']['PromptType'])))
            dialog_data[sid].append(str((js['Prompt']['Prompt'])))
            dialog_data[sid].append(str((js['Prompt']['TTSKey'])))
            dialog_data[sid].append(str((js['DialogTree']['DialogTreeName'])))
            dialog_data[sid].append(str((js['DialogTree']['DialogTreeIdx'])))
            dialog_data[sid].append(str((js['DialogTree']['DialogTreeNodeName'])))
            dialog_data[sid].append(str((js['DialogTree']['DialogTreeNodeIdx'])))
            dialog_data[sid].append(str((js['DialogTree']['DialogCurrentIntent'])))
            for dialogs in dialog_data:
                if len(dialog_data[dialogs]) > 15:
                    ls_all.extend(dialog_data[sid])
            # print("all_result:" + "\t" + "\t".join(ls_all))
            ls_all = []
            dialog_data.pop(sid)
