import os
import base64
import requests
import json
import time
import cv2


# 人脸检测
header = {
    "Token": "ae15bfd45069400c86d8f5571c521728"
}

if __name__ == '__main__':
    image = cv2.imread('./sd-101.jpg').tolist()
    url = "http://aiplatform-pbs-uat.inneryiche.com/arges/taskflow/infer"
    # input_data = {
    #     "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
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



























    # print(json.dumps(input_data))
    s_time = time.time()
    response = requests.post(url, json=input_data, headers=header).json()
    print(response)
    print(time.time() - s_time)
    assert response["code"] == 0
    # if response["code"] != 0:
    #     print("request fail !!!")
    #     print(response)
    # else:
    #     boxes = response["data"]["result"]["boxes"]
    #     scores = response["data"]["result"]["scores"]
    #     kpts = response["data"]["result"]["kpts"]
    #     for box, score, kp in zip(boxes, scores, kpts):
    #         x, y, w, h = box
    #     #     # Draw rectangle
    #         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), thickness=4)
    #         for i in range(5):
    #             cv2.circle(image, (int(kp[i * 3]), int(kp[i * 3 + 1])), 1, (0, 255, 0), thickness=-1)
    #     cv2.imwrite("result_1.jpg", image)
