import requests
import json
import base64
import argparse
import os
import numpy as np
import cv2
import sys
__dir__ = os.path.dirname(__file__)
__src__ = os.path.abspath(os.path.join(__dir__, '../src'))
sys.path.append(__src__)
print(__src__)
# from image_reader import read_image_heif


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='imgs/130718399_950.jpg')
    # parser.add_argument('--img_url', default='https://www2.autoimg.cn/newsdfs/g26/M08/1B/05/autohomecar__ChwFkGBuv9iAGlqWAANNH9AwVE4424.jpg')
    parser.add_argument('--img_url', default=None)
    # parser.add_argument('--url', default='http://127.0.0.1:9700/auto/recog')
    #parser.add_argument('--url', default='http://inner-model-car.yiche.com/auto/recog_multi')
    parser.add_argument('--url', default='http://10.168.47.16:19700/auto/recog_multi')
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
        files = [('file', (filename, open(args.input,'rb'), 'image/jpeg'))]

    response = requests.request("POST", args.url, headers=headers, data=payload, files=files)
    print(type(response.text))

    result = json.loads(response.text)
    print(type(result), result)

    with open(os.path.join(args.out_dir, filename + '.txt'), 'w') as fo:
        for d in result['data']:
            print("{}\t{}\n".format(d['box'], d['score']))
            fo.write("{}\t{}\n".format(d['box'], d['score']))
            for x in d['cls_result']:
                print('\t', x)
                fo.write('\t' + '\t'.join([str(i) for i in x]) + '\n')

    image_file = open(args.input, 'rb').read()
    # if whatimage.identify_image(image_file) in ['heic']:
    #     image_file = read_image_heif(image_file)
    img = cv2.imdecode(np.frombuffer(image_file, dtype=np.uint8), cv2.IMREAD_COLOR)
    # img = cv2.imread(args.input)
    height, width = img.shape[:2]

    for i, d in enumerate(result['data']):
        box = d['box'].copy()
        print(img.shape, box)
        box[0], box[2] = int(box[0] * width), int(box[2] * width)
        box[1], box[3] = int(box[1] * height), int(box[3] * height)
        cv2.imwrite(os.path.join(args.out_dir, filename + ".car.{}.jpg".format(i)), img[box[1]:box[3], box[0]:box[2]])

    for i, d in enumerate(result['data']):
        box = d['box'].copy()
        print(img.shape, box)
        box[0], box[2] = int(box[0] * width), int(box[2] * width)
        box[1], box[3] = int(box[1] * height), int(box[3] * height)
        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 3)
    cv2.imwrite(os.path.join(args.out_dir, filename + ".show.jpg"), img)


if __name__ == '__main__':
    main(get_args())

