import requests
import logging
import pdb
import json
import time

header = {
    "Token": "cc91ce4391de4fa7a66459fe3092e59e",
}

if __name__ == '__main__':
    import uuid

    print(str(uuid.uuid4()))
    url = "http://aiplatform-pbs-uat.inneryiche.com/arges/taskflow/infer"
    input_data = {
    "appId": "999318a6-778e-4ec4-b4b5-c2663be80e3b",
    "userId": "IN0010",
    "userRequestId": "222",
    "requestId": "1111",
    "data": {
        "info": {
            "news_id": "89757",
            "url": "123",
            "news_type": "news",
            "relate_serial_id": "大众",
            "relate_main_serial_id": "迈腾",
            "label": "123",
            "long_title": "",
            "content": "小小改装一下，贴了将近2个小时，买车选装了黑顶，现在把AB柱也贴黑，感觉挺有层次感，都说大众有奥迪气质，大众是奥迪平替，你们有这种感觉吗？",
            "style": "严谨",
            "char_len": {
                "max_len": 20,
                "min_len": 10
            },
            "model_type": "ycglm",
            "buis_id": "T012",
            "extra": {}
        }
    }
}
    # input_data = {
    #     "appId": "999318a6-778e-4ec4-b4b5-c2663be80e3b",
    #     "userId": "IN0010",
    #     "userRequestId": "222",
    #     "requestId": "1111",
    #     "data": {
    #         "info": {
    #             "news_id": "123",
    #             "url": "123",
    #             "news_type": "ugc",  # news, ugc, video
    #             "relate_serial_id": "123",
    #             "relate_main_serial_id": "123",
    #             "label": "123",
    #             "long_title": "123",
    #             "content": "小小改装一下，贴了将近2个小时，买车选装了黑顶，现在把AB柱也贴黑，感觉挺有层次感，都说大众有奥迪气质，大众是奥迪平替，你们有这种感觉吗？",
    #             "style": "严谨",
    #             "char_len": {
    #                 "max_len": 20,
    #                 "min_len": 10
    #             },
    #             "model_type": "ycglm",
    #             "buis_id": "T001",  # T001, T002, T999
    #             "extra": {},
    #         }
    #
    #     },
    #     "extra": {"rrrr": 666}
    # }
    s_time = time.time()
    response = requests.post(url, json=input_data, headers=header)
    # response = requests.post(url, json=input_data)
    output = json.loads(response.text)
    print(output)
    print(time.time() - s_time)