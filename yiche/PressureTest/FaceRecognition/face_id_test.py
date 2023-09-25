# -*- coding: utf-8 -*-

import base64
import requests
import json
import time
import cv2
import numpy as np

# 人脸特征抽取
header = {
    "Token": "ae15bfd45069400c86d8f5571c521728"
}


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b).T
    mul_a = np.linalg.norm(a, ord=2)
    mul_b = np.linalg.norm(b, ord=2)
    mul_ab = np.dot(a, b)
    return mul_ab / (mul_a * mul_b)


if __name__ == '__main__':
    image = cv2.imread('./sd-102.jpg').tolist()
    print(len(image))
    url = "http://aiplatform-pbs-uat.inneryiche.com/arges/taskflow/infer"
    input_data = {
        "appId": "6c73d673-ffdb-45c8-b54b-809d01a7d712",
        "userId": "IN0001",
        "userRequestId": "222",
        "data": {
            "info": {
                "img": image
            }
        }
    }
    # print(json.dumps(input_data))
    s_time = time.time()
    response = requests.post(url, json=input_data, headers=header).text
    print(response)
    print(time.time() - s_time)
    if response["code"] != 0:
        print("request fail !!!")
        print(response)
    else:
        emb = response["data"]["result"]["emb"]
        print("cos: ", cosine_similarity(emb, emb))
        print(emb)
