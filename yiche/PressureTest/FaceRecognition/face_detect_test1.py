from locust import HttpUser, task, TaskSet
import cv2

# pip install locust


class WebsiteTasks(TaskSet):

    @task
    def face_detect(self):
        header = {"Token": "ae15bfd45069400c86d8f5571c521728", "Content-Type": "application/json"}
        image = cv2.imread('./test_png13.png')
        url = "/arges/taskflow/infer"
        input_data = {
            "appId": "9dd3e603-2acf-414c-93a8-d7153f6c85ca",
            "userId": "IN0001",
            "userRequestId": "222",
            "data": {
                "info": {
                    "img": image.tolist()
                }
            }
        }
        import json
        response = self.client.post(url, data=json.dumps(input_data), headers=header)
        if response.status_code == 200:
            assert response.json().get("code") == 0
            if response.json().get("code") != 0:
                response.failure(f"断言失败，返回结果为：{response.json()}")
        else:
            response.failure(f"断言失败，接口状态码为：{response.status_code}")


class WebsiteUser(HttpUser):
    host = "http://aiplatform-pbs-uat.inneryiche.com"
    tasks = [WebsiteTasks]
    min_wait = 1000
    max_wait = 2000


if __name__ == '__main__':
    import os
    os.system("locust -f face_detect_test1.py")     # 在http://localhost:8089/ 查看结果，localhost可替换为服务器地址
    # os.system("locust -f face_detect_test1.py --headless -u 10 -r 10 -t 60 ")




