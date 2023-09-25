# -*- coding: utf-8 -*-

import json
import yaml
import os


def ddt(case_info):
    if "parameterize" in case_info.keys():
        case_info_str = json.dumps(case_info)
        for param_key, param_value in case_info["parameterize"].items():
            key_list = param_key.split("-")
            length_flag = True
            # 规范yaml数据文件的写法
            data_list = read_data(param_value)
            for data in data_list:
                # print(data)
                if len(data) != len(key_list):
                    length_flag = False
                    break
            new_case_info = []
            if length_flag:
                for x in range(1, len(data_list)):  # 循环数据的行数
                    temp_case_info = case_info_str
                    for y in range(0, len(data_list[x])):  # 循环数据列
                        if data_list[0][y] in key_list:
                            # 替换原始的yaml里面的$ddt{}
                            # 数字类型去掉“”
                            if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
                                temp_case_info = temp_case_info.replace('"$ddt{' + data_list[0][y] + '}"',
                                                                        str(data_list[x][y]))
                            else:
                                temp_case_info = temp_case_info.replace("$ddt{" + data_list[0][y] + "}",
                                                                        str(data_list[x][y]))
                    # print(temp_case_info)
                    new_case_info.append(json.loads(temp_case_info))
            return new_case_info
    else:
        return case_info


# 读取测试用例yaml文件
def read_case(yaml_path):
    with open(get_object_path() + yaml_path, 'r', encoding='utf-8') as f:
        case_info = yaml.load(stream=f, Loader=yaml.FullLoader)
        # 单纯复制修改参数的模式
        if len(case_info) >= 2:
            return case_info
        else:  # 有数据驱动的场合
            if "parameterize" in dict(*case_info).keys():
                new_case_info = ddt(*case_info)
                return new_case_info
            else:
                return case_info


# 获取项目根目录
def get_object_path():
    return os.path.abspath(os.getcwd().split("Common")[0])


# 读取yaml文件
def read_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 读取extract.yaml文件
def read_extract(key):
    with open(get_object_path() + "/extract.yaml", 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 写入extract.yaml文件
def write_extract(data):
    with open(get_object_path() + "/extract.yaml", 'a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


# 清除extract,yaml文件
def clear_extract():
    with open(get_object_path() + "/extract.yaml", 'w', encoding='utf-8') as f:
        f.truncate()


# 读取config.yaml文件
def read_config(one_nodo, two_node):
    with open(get_object_path() + "./Config/Config.yaml", 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[one_nodo][two_node]


# 读取数据的yaml
def read_data(yaml_path):
    with open(get_object_path() + '/Datas/' + yaml_path, 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


if __name__ == '__main__':
    pass
