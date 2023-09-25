# -*- coding: utf-8 -*-

import os
import requests
import argparse
import sys
import json
import time

__dir__ = os.path.dirname(__file__)
__src__ = os.path.abspath(os.path.join(__dir__, '../src'))
sys.path.append(__src__)
# print(__src__)
# from image_reader import read_image_heif


def get_args(path):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default=path)
    # parser.add_argument('--img_url', default='https://www2.autoimg.cn/newsdfs/g26/M08/1B/05/autohomecar__ChwFkGBuv9iAGlqWAANNH9AwVE4424.jpg')
    parser.add_argument('--img_url', default=None)
    # parser.add_argument('--url', default='http://127.0.0.1:19700/auto/recog')
    #parser.add_argument('--url', default='http://inner-model-car.yiche.com/auto/recog_multi')
    # parser.add_argument('--url', default='http://10.168.47.16:19700/auto/recog')  # 测试
    parser.add_argument('--url', default='http://inner-model-car.yiche.com/auto/recog')     # 生产
    parser.add_argument('--out_dir', default='./imgs_result')
    return parser.parse_args()


def main(args):
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)
    # print(args.url)
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
    return response


if __name__ == '__main__':
    model_cnt = 0
    test_cnt = 0
    success_cnt = 0
    failures_cnt = 0
    data = {}
    save_path = './identify_result.json'
    cars_model = os.listdir(os.getcwd() + '/cars_picture/')
    start_time = time.time()

    for models in cars_model:
        if os.path.isdir(os.getcwd() + '/cars_picture/' + models):
            cars = os.listdir(os.getcwd() + '/cars_picture/' + models)
            if len(cars) > 0:
                model_cnt += 1
                model = models.split('---')[1]
                model_id = models.split('---')[0]
                data[model] = {}
                for picture in cars:
                    path = os.getcwd() + '/cars_picture/' + models + '/' + picture
                    if os.path.isfile(path):
                        res = main(get_args(path))
                        test_cnt += 1
                        text_data = res.text
                        json_data = res.json()
                        if json_data["code"] == 0:
                            result = json_data["data"]["cls_result"]
                            print(model + ':' + str(result))
                            data[model][picture] = []
                            a = 0
                            for i in range(len(result)):
                                top = dict()
                                top[f"top{i+1}"] = {}
                                top[f"top{i+1}"]["score"] = result[i][0]
                                top[f"top{i+1}"]["result"] = result[i][2]
                                data[model][picture].append(top)
                                if model_id in result[i][2] and result[i][2].endswith(model):
                                    a += i+1
                                    success_cnt += 1
                                else:
                                    failures_cnt += 1
                            if a > 0:
                                data[model][picture].append(f"top{a}识别成功")
                            else:
                                data[model][picture].append("全部识别失败")
                        else:
                            data[model][picture] = {}
                            data[model][picture] = json_data
    data["analysis"] = {}
    data["analysis"]["车型总数"] = model_cnt
    data["analysis"]["照片总数"] = test_cnt
    data["analysis"]["识别成功总数"] = success_cnt
    data["analysis"]["识别总成功率"] = success_cnt / test_cnt
    print(data)
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    top1 = 0
    top2 = 0
    top3 = 0
    top4 = 0
    top5 = 0
    all_failure = 0
    not_found = 0
    with open(save_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data:
            if i != 'analysis':
                for y in data[i]:
                    if isinstance(data[i][y], list):
                        if data[i][y][-1] == 'top1识别成功':
                            top1 += 1
                        elif data[i][y][-1] == 'top2识别成功':
                            top2 += 1
                        elif data[i][y][-1] == 'top3识别成功':
                            top3 += 1
                        elif data[i][y][-1] == 'top4识别成功':
                            top4 += 1
                        elif data[i][y][-1] == 'top5识别成功':
                            top5 += 1
                        elif data[i][y][-1] == '全部识别失败':
                            all_failure += 1
                    else:
                        if isinstance(data[i][y], dict):
                            if 'code' in data[i][y].keys() and '没有找到车' in data[i][y]['message']:
                                not_found += 1
        data['analysis']['top1成功数'] = top1
        data['analysis']['top1成功率'] = top1 / data['analysis']['照片总数']
        data['analysis']['top2成功数'] = top2
        data['analysis']['top3成功数'] = top3
        data['analysis']['top4成功数'] = top4
        data['analysis']['top5成功数'] = top5
        data['analysis']['全部识别失败数'] = all_failure
        data['analysis']['未找到车型'] = not_found
        with open(save_path, 'w', encoding='utf-8') as ff:
            json.dump(data, ff, ensure_ascii=False, indent=4)
    end_time = time.time()
    print(f"花费时间：{end_time - start_time}")
