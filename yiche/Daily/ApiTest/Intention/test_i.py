import requests
import logging
import pdb
import json
import time

# header = {
#     "Inference-Header-Content-Length": "164",
# }


header = {
    "Token": "8a768549dbd142ecad01cbc2a83f78d9",
}

if __name__ == '__main__':
    #url = 'http://10.168.47.19:3000/arges/taskflow/infer'
    url = 'http://127.0.0.1:3000/arges/taskflow/infer'
    #url = 'http://10.168.47.19:11800/v2/models/t_single_2/versions/1/infer'
    #input_data = b'{"inputs":[{"name":"input","shape":[1,1],"datatype":"BYTES","parameters":{"binary_data_size":28}}],"outputs":[{"name":"output2","parameters":{"binary_data":true}}]}\x18\x00\x00\x00\xe6\xb5\x8b\xe8\xaf\x95\xe4\xb8\x80\xe4\xb8\x8b\xe4\xb8\xa4\xe4\xb8\xaa\xe6\xa8\xa1\xe5\x9e\x8b'
    input_data = {
        "appId": "5a59523f-c7d3-4dce-b08b-a560e63937ee",
        "userId": "OT0006",
        "userRequestId": "222",
        "requestId": "1111",
        "data": {
            "info": {
                "Common": {
                    "tenantId": "monitor",
                    "robotIdx": 1
                },
                "items": {
                    "1": {
                        "text": "今天天气真好",
                    }
                }
            }

        },
        "extra": {"test":1}
    }
    print(json.dumps(input_data))
    s_time = time.time()
    response = requests.post(url, json=input_data, headers=header)
    #response = requests.post(url, json=input_data)
    print(response.text)
    print(time.time() - s_time)

