import base64
import requests
import json
import time
import filetype
import soundfile as sf
import numpy as np
from scipy.io.wavfile import write
import uuid

header = {
    "Token": "1a70360151cf4236bb0eb636c3e2894c"
}


def get_file_type(file_path):
    kind = filetype.guess(file_path)
    if kind is None:
        print('无法猜测文件类型！')
        return
    return kind.extension


if __name__ == '__main__':
    # url = "http://aiplatform-gn-test.yiche.com/arges/taskflow/infer"
    # url = "http://yxtts-1-yxtts-1-prod.ga-business.bitautotech.com/algosrv/ttssrv"
    url = "http://aiplatform-gn-uat.inneryiche.com/yxtts"
    text10 = '您好非常高兴为您服务'
    text50 = '晋太元中，武陵人捕鱼为业。缘溪行，忘路之远近。忽逢桃花林，夹岸数百步，中无杂树，芳草鲜美，落英缤纷。'
    text116 = '东晋太元年间，武陵有个人以捕鱼为生。有一天他沿着溪水划船而行，忘记了路有多远。忽然遇到一片桃花林，在小溪两岸的几百步之内，中间没有其它树木，花草鲜嫩美丽，地上的落花繁多交杂，渔人对此感到非常诧异。他继续向前行船，想要走到林子的尽头。'
    text122 = '您好,这里是易鑫客服热线，您的提前还款申请已成功，请您务必在当天的15: 20之前打款至约定账户，完成还款后切记立即电话通知4000598598客服报备，以保证提前还款顺利完成，如有疑问，详询客服热线4000-598-598，感谢您的接听，再见！'
    text150 = '南山经中的第一列山系，名叫鹊山。鹊山的首座山，名叫招摇山。它紧靠西海，山上长有许多桂树，还有许多金和玉。山中有一种草，形状像韭菜，开青色的花，名字叫祝余，人吃了它，就不会感到饥饿。山中还长有一种树，它的形状像构树，树上有黑色的纹理，开的花能发光，可以照亮四周，它的名字叫迷榖，把它佩戴在身上就不会迷路'
    c38 = '您好，我们是汽车资讯平台，有各个汽车品牌的信息，来电就是想了解一下您的购车需求，以便有优惠活动的时候推荐给您。请问您近期考虑买车吗？'
    bq = '很抱歉打扰到您了，如果您不方便接听，我们就先不打扰了。祝您生活愉快！'
    c59 = '您之前有登陆过汽车网站或看过相关广告，我们来电是想简单了解下您的购车需求，以便有优惠活动时推荐给您。请问您最近在汽车平台留手机号咨询过汽车吗？比如汽车之家、易车、懂车帝之类的？ '
    input_data = {
        "appId": "d360b134-9805-48ba-a4bb-f9e3675f48cd",
        "userId": "OT0007",
        "userRequestId": "localpanxb",  # str(uuid.uuid1()),
        "data": {
            "info": {
                "Action": "TextToSpeech",
                "Version": "2023-08-23",  # ["2022-09-26", "2023-08-23"]
                # "Text": "您好，请问是刘德华先生吗？您在易鑫集团办理的业务本次需要还款2392.12元。请您尽量按时足额还款哦。",
                # "Text": "再见",
                "Text": text10,
                "SessionId": "test_panxb",
                "Volume": 1,
                "Speed": 1,
                # "ModelType": "",
                "VoiceType": 99910002,
                # "PrimaryLanguage": "",
                "SampleRate": 16000,
                "Codec": "mp3",
                "CutMerge": 0
            },
        }
    }
    # print(json.dumps(input_data))
    s_time = time.time()
    response = requests.post(url, json=input_data, headers=header)
    print(response.text)
    print(time.time() - s_time)
    response = response.json()

    save_filename = '0901_test_10002_16000.mp3'
    print(f"save_filename: {save_filename}")
    print(f"length: {len(input_data['data']['info']['Text'])}")
    decoded_data = base64.b64decode(response["data"]["info"]["Audio"].encode('ascii'))
    import io

    audio_stream = io.BytesIO(decoded_data)
    with open(save_filename, "wb") as f:
        f.write(audio_stream.getbuffer())
    file_type = get_file_type(save_filename)
    print('文件类型是:', file_type)
    audio_data, s_rate = sf.read(save_filename)
    print("采样率是：", s_rate)








