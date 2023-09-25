# -*- coding: utf-8 -*-

from locust import HttpUser, task, TaskSet
import os
import json

# pip install locust


class WebsiteTasks(TaskSet):

    @task
    def tts_test(self):
        header = {"Token": "1a70360151cf4236bb0eb636c3e2894c", "Content-Type": "application/json"}
        url = "/arges/taskflow/infer"
        input_data = {
            "appId": "d360b134-9805-48ba-a4bb-f9e3675f48cd",
            "userId": "OT0007",
            "userRequestId": "222",
            "data": {
                "info": {
                    "Action": "TextToSpeech",
                    "Text": "南山经之首，曰鹊山。其首曰招摇之山，临于西海之上，多桂，多金玉。有草焉，其状如韭而青华，其名曰祝余，食之不饥。有木焉，其状如榖而黑理，其华四照，其名曰迷榖，佩之不迷。有兽焉，其状如禺而白耳，伏行人走，其名曰狌狌，食之善走。丽麂之水出焉，而西流注于海，其中多育沛，佩之无瘕疾。",
                    "SessionId": "test_panxb",
                    "Volume": 3,
                    "Speed": 0.8,
                    "VoiceType": 1001,
                    "SampleRate": 24000,
                    "Codec": "WAV",
                    "CutMerge": 0
                }
            }
        }

        response = self.client.post(url, data=json.dumps(input_data), headers=header)
        if response.status_code == 200:
            assert response.json().get("code") == 0
            if response.json().get("code") != 0:
                response.failure(f"断言失败，返回结果为：{response.json()}")
        else:
            response.failure(f"断言失败，接口状态码为：{response.status_code}")


class WebsiteUser(HttpUser):
    host = "http://aiplatform-gn-test.yiche.com"
    tasks = [WebsiteTasks]
    min_wait = 1000
    max_wait = 2000


if __name__ == '__main__':
    # os.system("locust -f TTs_pt.py")  # 在http://localhost:8089/ 查看结果，localhost可替换为服务器地址
    os.system("locust -f TTs_pt.py --headless -u 10 -r 10 -t 60 ")
