import requests
import json
import base64
import argparse
import os
import numpy as np
# import cv2
import sys

__dir__ = os.path.dirname(__file__)
__src__ = os.path.abspath(os.path.join(__dir__, '../src'))
sys.path.append(__src__)
print(__src__)
# from image_reader import read_image_heif


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='cars_picture/8238---北汽家宝/北汽家宝左前.jpg')
    # parser.add_argument('--img_url', default='https://www2.autoimg.cn/newsdfs/g26/M08/1B/05/autohomecar__ChwFkGBuv9iAGlqWAANNH9AwVE4424.jpg')
    parser.add_argument('--img_url', default=None)
    # parser.add_argument('--url', default='http://127.0.0.1:19700/auto/recog')
    #parser.add_argument('--url', default='http://inner-model-car.yiche.com/auto/recog_multi')
    # parser.add_argument('--url', default='http://10.168.47.16:19700/auto/recog')    # 测试
    parser.add_argument('--url', default='http://inner-model-car.yiche.com/auto/recog')     # 生产
    # 生产host  10.20.15.3 inner-model-car.yiche.com
    parser.add_argument('--out_dir', default='./imgs_result')
    return parser.parse_args()


def main(args):
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    print(args.url)
    filename = os.path.basename(args.input)
    payload = {}
    headers = {}
    files = []
    if args.img_url:
        payload = {'img_url': args.img_url}
    else:
        files = [('file', (filename, open(args.input, 'rb'), 'image/jpeg'))]

    response = requests.request("POST", args.url, headers=headers, data=payload, files=files)
    # print(type(response.text))
    #
    # result = json.loads(response.text)
    # print(type(result), result)
    print(response.json())


if __name__ == '__main__':
    main(get_args())

