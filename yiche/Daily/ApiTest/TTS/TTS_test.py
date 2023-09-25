# -*- coding: utf-8 -*-

import base64
import requests
import json
import time
import os
import io
import datetime
import numpy as np
import filetype
import soundfile as sf
from scipy.io.wavfile import write


header = {"Token": "1a70360151cf4236bb0eb636c3e2894c"}


def get_file_type(file_path):
    kind = filetype.guess(file_path)
    if kind is None:
        print('无法猜测文件类型！')
        return
    return kind.extension


text1 = '好'

text10 = '您好非常高兴为您服务'

text50 = '晋太元中，武陵人捕鱼为业。缘溪行，忘路之远近。忽逢桃花林，夹岸数百步，中无杂树，芳草鲜美，落英缤纷。'

text116 = '东晋太元年间，武陵有个人以捕鱼为生。有一天他沿着溪水划船而行，忘记了路有多远。忽然遇到一片桃花林，在小溪两岸的几百步之内，中间没有其它树木，花草鲜嫩美丽，地上的落花繁多交杂，渔人对此感到非常诧异。他继续向前行船，想要走到林子的尽头。'

text150 = '南山经中的第一列山系，名叫鹊山。鹊山的首座山，名叫招摇山。它紧靠西海，山上长有许多桂树，还有许多金和玉。山中有一种草，形状像韭菜，开青色的花，名字叫祝余，人吃了它，就不会感到饥饿。山中还长有一种树，它的形状像构树，树上有黑色的纹理，开的花能发光，可以照亮四周，它的名字叫迷榖，把它佩戴在身上就不会迷路'


if __name__ == '__main__':
    # url = "http://aiplatform-gn-test.yiche.com/arges/taskflow/infer"  # 测试
    url = "http://aiplatform-pbs.inneryiche.com/arges/taskflow/infer"     # 生产
    day = datetime.date.today().strftime('%m%d')
    speaker = [1001, 1002, 1003]
    formats = ['wav', 'mp3']
    sample_rate = [8000, 16000, 24000]
    for s in speaker:
        for f in formats:
            for sr in sample_rate:
                input_data = {
                    "appId": "d360b134-9805-48ba-a4bb-f9e3675f48cd",
                    "userId": "OT0007",
                    "userRequestId": "222",
                    "data": {
                        "info": {
                            "Action": "TextToSpeech",
                            "Text": text150,
                            # "Text": "您好，我是芒果金融合作机构易鑫集团的服务顾问，请问是张小明先生吗",
                            "SessionId": "test_panxb",
                            "Volume": 1,
                            "Speed": 1,
                            "VoiceType": s,
                            "SampleRate": sr,
                            "Codec": f,
                            "CutMerge": 0
                        }
                    }
                }

                if 'gn' in url:
                    server = 'gn'
                else:
                    server = 'pbs'
                sound_dir = os.path.dirname(__file__) + f'/{server}_{day}_{s}_{f}'
                if not os.path.isdir(sound_dir):
                    os.mkdir(sound_dir)
                save_filename = sound_dir + f"/{day}_test_{sr}.{f}"
                response = requests.post(url, json=input_data, headers=header)
                response = response.json()
                decoded_data = base64.b64decode(response["data"]["info"]["Audio"].encode('ascii'))
                audio_stream = io.BytesIO(decoded_data)
                with open(save_filename, "wb") as s_f:
                    s_f.write(audio_stream.getbuffer())
                if os.path.isfile(save_filename):
                    file_type = get_file_type(save_filename)
                    print('文件类型是:', file_type)
                    audio_data, s_rate = sf.read(save_filename)
                    print("采样率是：", s_rate)
