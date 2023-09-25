# -*- coding: utf-8 -*-
from builtins import Exception
import logging
from logging import handlers
import datetime
import os
import time

file_log_level = 'info'
console_log_level = 'info'


def create_log(logger_name='log'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        file_log_path = os.getcwd() + "/Logs/" + "baichuan.log"
        # file_log_path = os.getcwd() + "/Logs/" + str(datetime.date.today()) + ".log"
        if not os.path.isdir(os.getcwd() + "/Logs/"):
            os.mkdir(os.getcwd() + "/Logs/")
        file_handler = handlers.TimedRotatingFileHandler(filename=file_log_path, when='MIDNIGHT', backupCount=7, encoding='utf-8')
        if file_log_level == "info":
            file_handler.setLevel(logging.INFO)
        elif file_log_level == "error":
            file_handler.setLevel(logging.ERROR)

        # 4.创建文件日志格式
        file_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s'))
        # 将文件日志的控制器加入到日志对象
        logger.addHandler(file_handler)
        # -------控制台日志----------
        # 1.创建控制台日志的控制器
        console_handler = logging.StreamHandler()
        # 2.创建控制台日志的日志级别
        if console_log_level == "info":
            console_handler.setLevel(logging.INFO)
        elif console_log_level == "error":
            console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s'))
        logger.addHandler(console_handler)
    return logger


if __name__ == '__main__':
    while True:
        create_log().info('test')
        time.sleep(1)
