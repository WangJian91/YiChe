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

# args = sys.argv
args = ['', './0509/2023-05-09-res_pure', '0505']
f_r = open(args[1], "r")


def findAllFile(base,conv,msg):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            fullname_trans = fullname.strip().replace(" ", "")
            if(fullname_trans.find(conv)>-1 and fullname_trans.find(msg)>-1):
                from xpinyin import Pinyin
                p = Pinyin()
                result1 = p.get_pinyin(msg)
                fullname_trans_pinyin = fullname_trans.replace(msg, result1)
                os.rename(fullname, fullname_trans_pinyin)
                return fullname_trans_pinyin
    str = ""
    return str

conv_dic = dict()
with open(args[1], 'r') as fcc_file:
    for line in fcc_file.readlines():
        datas = line.strip().split("\t")
        ls_tmp = []
        # print(f'Datas:{Datas}')
        if(datas[0] in conv_dic):
            ls_tmp = conv_dic[datas[0]]
            # print(ls_tmp)
        # print(Datas[1])
        if(datas[1]==""):
            tp_dic = dict()
            tp_dic["from_who"] = "agent"
            tp_dic["msg"] = datas[3]
            # print(tp_dic)
            ls_tmp.append(tp_dic)
            # print(ls_tmp)
        else:
            tp_dic = dict()
            tp_dic["from_who"] = "user"
            tp_dic["msg"] = datas[1]
            tp_dic["intent"] = datas[2]
            ls_tmp.append(tp_dic)
            tp_dic = dict()
            tp_dic["from_who"] = "agent"
            tp_dic["msg"] = datas[3]
            # print(tp_dic)
            ls_tmp.append(tp_dic)
        conv_dic[datas[0]] = ls_tmp

js = []
with open(args[1], 'r') as fcc_file:
    for line in fcc_file.readlines():
        datas = line.strip().split("\t")
        if(datas[1] == ""):
            continue
        fullname = findAllFile("./"+args[2]+"/",datas[0],datas[1])
        # print(fullname)
        if(fullname == ""):
            continue

        str_tre = ""
        str_tre = str_tre + "audio_msg:"+datas[1]+"\n"
        str_tre = str_tre + "\n"
        for di in conv_dic[datas[0]]:
            if("intent" in di):
                str_tre = str_tre + di["from_who"]+":"+di["msg"]+"    intent:"+di["intent"]+"\n"
            else:
                str_tre = str_tre + di["from_who"]+":"+di["msg"]+"\n"
        single = {
            "data":{
                "audio": "/label_studio/data/local-files/?d=xj_wh_voice/"+fullname.replace("./","").replace("\\","/"),
                "convd": str_tre
            }
        }
        js.append(single)
print(json.dumps(js))

