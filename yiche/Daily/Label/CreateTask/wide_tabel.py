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
# f_r = open(args, "r", encoding='utf-8')


with open(args, 'r', encoding='utf-8') as fcc_file:
    ls_all = []
    for line in fcc_file.readlines():
        ls_req_param = []
        if(line.find("DialogCore: param: {")>-1):
            trace_id = str(uuid.uuid1())
            datas= line.strip().split("DialogCore: param:")
            js = json.loads(datas[1].strip().replace("None", "\"\"").replace("\'", "\""))
            # print(js)
            ls_req_param.append(str(js['sessionIdx']))
            ls_req_param.append(str(trace_id))
            ls_req_param.append(str(js['inParams']['tenantIdx']))
            ls_req_param.append(str(js['inParams']['robotIdx']))
            ls_req_param.append(str(js['inAction']))
            #print("req_param"+"\t"+"\t".join(ls_req_param))
            ls_all.extend(ls_req_param)
        ls_nlu_res = []
        if(line.find("nlu result: time:")>-1):
            datas= line.strip().split("nlu result:")

            # print(Datas[-1])
            #print(Datas[-1].replace("\'", "\"").replace("\"Confirm\": False",
            #                                            "\"Confirm\": \"False\"").replace("\"Confirm\": True",
            #                                            "\"Confirm\": \"True\"").replace("Idon\"t","Idont"))
            js = json.loads(datas[-1].replace("\'", "\"").replace("\"Confirm\": False",
                                                        "\"Confirm\": \"False\"").replace("\"Confirm\": True",
                                                        "\"Confirm\": \"True\"").replace("Idon\"t",
                                                        "Idont").replace("Idon\"","Idon").replace("what\"syourname",

                                                        "whatsyourname"))

            ls_nlu_res.append(str(js['UserAction']))
            ls_nlu_res.append(str(js['Utter']))
            ls_nlu_res.append(str(js['Intents'][0]['IntentName']))
            ls_nlu_res.append(str(js['Intents'][0]['IntentIdx']))
            ls_nlu_res.append(str(js['Intents'][0]['IntentConf']))
            #print("nlu_result:"+"\t"+"\t".join(ls_nlu_res))
            ls_all.extend(ls_nlu_res)
        ls_dm_res = []
        if(line.find("dm result:time:")>-1):
            datas= line.strip().split("dm result:")
            # print(Datas[-1])
            js = json.loads(datas[-1].replace("\'", "\"").replace("False","\"False\"").replace("True","\"True\""))
            ls_dm_res.append(str((js['ExecuteActionType'])))
            ls_dm_res.append(str((js['Prompt']['PromptType'])))
            ls_dm_res.append(str((js['Prompt']['Prompt'])))
            ls_dm_res.append(str((js['Prompt']['TTSKey'])))
            ls_dm_res.append(str((js['DialogTree']['DialogTreeName'])))
            ls_dm_res.append(str((js['DialogTree']['DialogTreeIdx'])))
            ls_dm_res.append(str((js['DialogTree']['DialogTreeNodeName'])))
            ls_dm_res.append(str((js['DialogTree']['DialogTreeNodeIdx'])))
            ls_dm_res.append(str((js['DialogTree']['DialogCurrentIntent'])))
            #print("dm_result:"+"\t"+"\t".join(ls_dm_res))
            # print(ls_dm_res)
            ls_all.extend(ls_dm_res)
            print(ls_all)
            # print("all_result:"+"\t"+"\t".join(ls_all))
            ls_all = []



