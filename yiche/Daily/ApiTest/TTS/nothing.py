# -*- coding: utf-8 -*-

import datetime
import filetype
import sys
import os
import re
import soundfile as sf
import magic


def get_file_type(file_path):
    kind = filetype.guess(file_path)
    if kind is None:
        print('无法猜测文件类型！')
        return
    return kind.extension


if __name__ == '__main__':
    # save_filename = "./0829_test_1002_16000.mp3"
    # file_type = get_file_type(save_filename)
    # print('文件类型是:', file_type)
    # audio_data, sample_rate = sf.read(save_filename)
    # print("采样率：", sample_rate)
    pass













