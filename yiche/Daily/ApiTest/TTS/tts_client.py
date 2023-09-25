import base64
import requests
import json
import time
import io
import datetime
import os
import sys
import numpy as np
import filetype
import soundfile as sf
from scipy.io.wavfile import write

header = {
    "Token": "1a70360151cf4236bb0eb636c3e2894c"
}


def get_file_type(file_path):
    kind = filetype.guess(file_path)
    if kind is None:
        print('无法猜测文件类型！')
        return
    return kind.extension


text150 = '南山经中的第一列山系，名叫鹊山。鹊山的首座山，名叫招摇山。它紧靠西海，山上长有许多桂树，还有许多金和玉。山中有一种草，形状像韭菜，开青色的花，名字叫祝余，人吃了它，就不会感到饥饿。山中还长有一种树，它的形状像构树，树上有黑色的纹理，开的花能发光，可以照亮四周，它的名字叫迷榖，把它佩戴在身上就不会迷路'

text_n = '您好，请问是{刘德华}{先生}吗？您在易鑫集团办理的业务本次需要还款{2392.12}元。请您尽量按时足额还款哦。'

if __name__ == '__main__':
    # url = "http://aiplatform-gn-test.yiche.com/arges/taskflow/infer"
    url = "http://aiplatform-pbs.inneryiche.com/arges/taskflow/infer"
    input_data = {
        "appId": "d360b134-9805-48ba-a4bb-f9e3675f48cd",
        "userId": "OT0007",
        "userRequestId": "222",
        "data": {
            "info": {
                "Action": "TextToSpeech",
                # "Version": "",
                # "Text": "您好，我是芒果金融合作机构易鑫集团的服务顾问，请问是张小明先生吗",
                "Text": text_n,
                "SessionId": "test_panxb",
                "Volume": 1,
                "Speed": 1,
                # "ModelType": "",
                "VoiceType": 1002,
                # "PrimaryLanguage": "",
                "SampleRate": 8000,
                "Codec": "mp3",
                "CutMerge": 0
            },
        }
    }
    # print(json.dumps(input_data))
    s_time = time.time()
    response = requests.post(url, json=input_data, headers=header)
    # print(response.text)
    print(time.time() - s_time)
    response = response.json()
    save_filename = "./0825_test_8000.mp3"
    print(f"save_filename: {save_filename}")
    decoded_data = base64.b64decode(response["data"]["info"]["Audio"].encode('ascii'))
    audio_stream = io.BytesIO(decoded_data)
    with open(save_filename, "wb") as f:
        f.write(audio_stream.getbuffer())
    file_type = get_file_type(save_filename)
    print('文件类型是:', file_type)
    audio_data, sample_rate = sf.read(save_filename)
    print("采样率是：", sample_rate)




