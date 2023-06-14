
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
    image = cv2.imread('./xx.png').tolist()
    # print(len(image))
    url = "http://aiplatform-pbs-uat.inneryiche.com/arges/taskflow/infer"
    # input_data = {
    #     "appId": "6c73d673-ffdb-45c8-b54b-809d01a7d712",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": image
    #         }
    #     }
    # }   # 正确参数

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca1",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": image
    #         }
    #     }
    # }   # appId错误

    # input_data = {
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": image
    #         }
    #     }
    # }   # appId缺失

    # input_data = {
    #     "appId": "",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": image
    #         }
    #     }
    # }   # appId为空

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "wang",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": image
    #         }
    #     }
    # }   # userId错误

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": image
    #         }
    #     }
    # }   # userId为空

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": image
    #         }
    #     }
    # }   # userId缺失

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {'1': 2
    #     }
    # }   # data参数错误

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #     }
    # }   # data为空

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    # }   # data缺失

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {'1': 2}
    #     }
    # }   # info参数错误

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #         }
    #     }
    # }   # info为空

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #     }
    # }   # info缺失

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": 1
    #         }
    #     }
    # }   # img参数错误

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": []
    #         }
    #     }
    # }   # img为空

    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #         }
    #     }
    # }   # img缺失

    # input_data = {
    #     "appId": "6c73d673-ffdb-45c8-b54b-809d01a7d712",
    #     "userId": "IN0001",
    #     "userRequestId": "222",
    #     "data": {
    #         "info": {
    #             "img": image
    #         }
    #     }
    # }   # 正确参数

    s_time = time.time()
    response = requests.post(url, json=input_data, headers=header).json()
    print(response)
    print(time.time() - s_time)

