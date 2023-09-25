# -*- coding: utf-8 -*-

import json

num = 0
with open("./case_result.json", "r", encoding="utf-8") as f:
    for i in json.load(f):
        if "data" in i.keys():
            if i["label_en"] not in i["action_result"]:
                num += 1
                with open("./analyse_result.txt", "a", encoding="utf-8")as an:
                    an.write(str(num) + '、' + i["data"]["question"] + '\n')
                    an.write('预期：' + i["label_en"] + '\n')
                    an.write('实际：' + i["action_result"] + '\n' + '-'*50 + '\n')
