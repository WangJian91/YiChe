# -*- coding: utf-8 -*-
"""
loguru 封装类，导入即可直接使用
# 当前文件名 loggeruru.py
"""

import os
os.environ["LOGURU_AUTOINIT"] = "0"

from functools import wraps
import loguru
import configparser


# 单例类的装饰器
def singleton_class_decorator(cls):
    """
    装饰器，单例类的装饰器
    """
    # 在装饰器里定义一个字典，用来存放类的实例。
    _instance = {}

    # 装饰器，被装饰的类
    @wraps(cls)
    def wrapper_class(*args, **kwargs):
        # 判断，类实例不在类实例的字典里，就重新创建类实例
        if cls not in _instance:
            # 将新创建的类实例，存入到实例字典中
            _instance[cls] = cls(*args, **kwargs)
        # 如果实例字典中，存在类实例，直接取出返回类实例
        return _instance[cls]

    # 返回，装饰器中，被装饰的类函数
    return wrapper_class


@singleton_class_decorator
class Logger:
    # ./utils_api/logutil/
    def __init__(self, logconfigpath="loguru.ini"):
        if len(loguru.logger.__str__().split('),')) <= 1:
            print('loguru 开始初始化')
            self.logger_add(logconfigpath)
        else:
            print('loguru 已初始化')

    def get_log_conf(self, file):
        c = configparser.ConfigParser()
        read_ok = c.read(os.path.join(os.path.dirname(__file__), file), encoding="utf-8-sig")
        # print("read_ok:",read_ok)
        if len(read_ok) == 0:
            raise Exception("Read ini failed!!!")

        # 默认配置
        section = 'default'
        dict_default = {}
        dict_default['format'] = c.get(section, 'format', fallback=loguru._defaults.LOGURU_FORMAT)
        dict_default['filter'] = None
        dict_default['rotation'] = c.get(section, 'rotation', fallback='00:00')
        dict_default['retention'] = c.get(section, 'retention', fallback='1 months')
        dict_default['compression'] = c.get(section, 'compression', fallback=None)
        dict_default['encoding'] = c.get(section, 'encoding', fallback='utf-8')
        dict_default['enqueue'] = c.get(section, 'enqueue', fallback=True)
        dict_default['level'] = c.get(section, 'level', fallback='INFO')
        default_filepath = c.get(section, 'file', fallback=None)
        # default_filepath = "/c_models/call_cpu_process/analysis_call/Utils"
        if default_filepath == '': default_filepath = None
        dict_default['filepath'] = default_filepath

        list_out = []
        for sec in c.sections():
            if sec == 'default':
                continue

            dict = {}
            dict['format'] = c.get(sec, 'format', fallback=dict_default['format'])
            dict['rotation'] = c.get(sec, 'rotation', fallback=dict_default['rotation'])
            dict['retention'] = c.get(sec, 'retention', fallback=dict_default['retention'])
            dict['compression'] = c.get(sec, 'compression', fallback=dict_default['compression'])
            dict['encoding'] = c.get(sec, 'encoding', fallback=dict_default['encoding'])
            dict['enqueue'] = c.get(sec, 'enqueue', fallback=dict_default['enqueue'])
            dict['level'] = c.get(sec, 'level', fallback=dict_default['level'])

            # 过滤方式
            filter_type = str.strip(c.get(sec, 'filter_type', fallback='None'))
            filter_str = str.strip(c.get(sec, 'filter_str', fallback=''))
            filter = None
            if filter_type == 'None' or filter_str == '':
                filter = None
            elif filter_type == 'Bind':
                # 粒度匹配，使用logger.bind(xxx=True).info()
                filter = lambda record: filter_str in record["extra"]
            elif filter_type == 'NotBind':
                filter = lambda record: filter_str not in record["extra"]
            elif filter_type == 'Match':
                # 使用字符串模糊匹配过滤
                filter = lambda x: filter_str in x['message']
            elif filter_type == 'NotMatch':
                filter = lambda x: filter_str not in x['message']
            else:
                filter = None
            dict['filter'] = filter

            # 日志文件位置
            filepath = ''
            if str.strip(c.get(sec, 'file', fallback='')) != '':
                filepath = c.get(sec, 'file')
                # /c_models/call_cpu_process/analysis_call/LogData
            elif dict_default['filepath'] is not None:
                filepath = dict_default['filepath']
            else:
                # 日志和当前目录平级
                filepath = os.path.join(os.path.dirname(__file__), '..', 'logs', sec + '.log')
            # filepath = "/c_models/call_cpu_process/analysis_call/Utils"
            dict['filepath'] = filepath
            list_out.append(dict)
        return list_out

    def logger_add(self, logconfigpath):
        # 读取配置文件
        # list = self.get_log_conf("loguru.ini")
        list = self.get_log_conf(logconfigpath)
        print(f"--- log list == {list} ---")
        for dict in list:
            loguru.logger.add(
                # 水槽，分流器，可以用来输入路径
                sink=dict['filepath'],
                # 格式化
                format=dict['format'],
                # 日志创建周期, 目前看不支持同时按时间和大小分割
                rotation=dict['rotation'],
                # 保存
                retention=dict['retention'],
                # 文件的压缩格式
                compression=dict['compression'],
                # 编码格式
                encoding=dict['encoding'],
                # 具有使日志记录调用非阻塞的优点
                enqueue=dict['enqueue'],
                # 过滤器
                filter=dict['filter'],
                # 日志级别
                level=dict['level'],
                # 错误栈
                backtrace=True,
                diagnose=True,
                context="spawn"
            )

    @property
    def get_logger(self):
        return loguru.logger


'''
# 实例化日志类
'''
# logger1 = Logger().get_logger
# ul = logger1.bind(reqid='None').bind(user="None").bind(web=True)
# logger1 = logger.bind(special=True)
# # 输出到module1.log
# logger1.info('123 bind special')
# logger.bind(module1=True).info('456 bind module1')