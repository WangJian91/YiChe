# -*- coding: utf-8 -*-

from ConversationTree.Common.logger_util import error_log, logs
from ConversationTree.Common.parameterize_util import *
import json
import re
import traceback
import jsonpath
import requests


class RequestsUtil:
    session = requests.session()

    def __init__(self, obj):
        self.obj = obj

    # 规范YAML测试用例
    def standard_yaml(self, case_info):
        try:
            case_info_key = case_info.keys()
            if "name" in case_info_key and "request" in case_info_key and "validate" in case_info_key:
                request_keys = case_info["request"].keys()
                if "method" in request_keys and "url" in request_keys:
                    name = case_info.pop("name")
                    base_url = read_config("base", "base_test_url")
                    method = case_info["request"].pop("method")
                    url = case_info["request"].pop("url")
                    self.headers = case_info["request"].pop("headers")
                    data = case_info["request"]
                    res = self.send_request(name, method, base_url + url, **data)
                    result_text = res.text
                    result_code = res.status_code
                    result_json = ""
                    try:
                        result_json = res.json()
                    except Exception:
                        print("extract返回的结果不是JSON格式,不能使用jsonpath提取")
                    # 提取值并且写入extarct.yaml文件
                    # if "extract" in case_info.keys():
                    #     for key, value in case_info["extract"].items():
                    #         if "(.*?)" in value or "(.+?)" in value:  # 正则表达式
                    #             zz_value = re.search(value, result_text)
                    #             if zz_value:
                    #                 extract_value = {key: zz_value.group(1)}
                    #                 write_extract(extract_value)
                    #         else:  # jsonpath
                    #             js_value = jsonpath.jsonpath(result_json, value)
                    #             if js_value:
                    #                 extract_value = {key: js_value[0]}
                    #                 write_extract(extract_value)
                    # 断言
                    self.assert_result(case_info["validate"], result_json, result_code)
                else:
                    print("在request下必需包含：method,url")
            else:
                print("一级关键字必须要包含：name,request,validate")
        except Exception:
            error_log("规范YAML测试用例standard_yaml异常：%s" %
                      str(traceback.format_exc()))

    def replace_value(self, data):
        if data:
            # 保存数据类型
            data_type = type(data)
            # 判断数据类型
            if isinstance(data, dict) or isinstance(data, list):
                str_data = json.dumps(data)
            else:
                str_data = str(data)
            # 替换
            for cs in range(1, str_data.count('${') + 1):
                if "${" in str_data and "}" in str_data:
                    start_index = str_data.index("${")
                    end_index = str_data.index("}", start_index)
                    old_value = str_data[start_index:end_index + 1]
                    # 反射：通过字类的对象和方法符串调用方法
                    func_name = old_value[2:old_value.index("(")]
                    args_value1 = old_value[old_value.index("(") + 1:old_value.index(")")]
                    if args_value1 != "":
                        if "," in args_value1:
                            args_value2 = args_value1.split(",")
                            new_value = getattr(self.obj, func_name)(*args_value2)
                        else:
                            new_value = getattr(
                                self.obj, func_name)(args_value1)
                    else:
                        new_value = getattr(self.obj, func_name)
                    # 数字类型去掉“”
                    if isinstance(new_value, int) or isinstance(
                            new_value, float):
                        str_data = str_data.replace(
                            '"' + old_value + '"', str(new_value))
                    else:
                        str_data = str_data.replace(old_value, str(new_value))
            # 还原数据类型
            if isinstance(data, dict) or isinstance(data, list):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
        return data

    # 统一请求封装
    def send_request(self, name, method, url, **data):
        try:
            logs("--------接口测试开始--------")
            # 请求头和参数替换
            for key, value in data.items():
                if key in ["params", "data", "json", "headers"]:
                    data[key] = self.replace_value(value)
                elif key == "files":
                    for file_key, file_path in value.items():
                        value[file_key] = open(file_path, "rb")
                # 输入信息日志
                logs("请求名称：%s" % name)
                logs("请求方式：%s" % method)
                logs("请求路径：%s" % url)
                logs("请求头：%s" % self.headers)
                if "params" in data.keys():
                    logs("请求params参数：%s" % data["params"])
                elif "data" in data.keys():
                    logs("请求data参数：%s" % data["data"])
                elif "json" in data.keys():
                    if data["json"]["inAction"] == 1:
                        logs("请求参数：%s" % data["json"]["inParams"]["userInfo"])
                    if data["json"]["inAction"] == 2:
                        logs("请求参数：%s" % data["json"]["inParams"]["input"])
                if "files" in data.keys():
                    logs("请求files参数：%s" % data["files"])
                # 发送请求
                header = self.headers
                data = json.dumps(data["json"])
                rep = RequestsUtil.session.request(method, url, headers=header, data=data)
                # print(rep.json())
                return rep
        except Exception:
            error_log("发送请求send_request异常：%s" % str(traceback.format_exc()))

    def assert_result(self, yq_result, sj_result, result_code):
        try:
            if isinstance(yq_result[0]["equals"], str):
                logs("预期结果：%s" % yq_result[0]["equals"])
            # if isinstance(yq_result[0]["equals"], dict):
            #     robot = read_config("system", "robot")
            #     logs("预期结果：%s" % yq_result[0]["equals"][str(robot)])
            # print(sj_result)
            logs("实际结果：%s" % json.loads(json.dumps(sj_result[0]["outParam"]["promptText"]).replace(r"\\", "\\")))
            all_flag = 0
            for yq in yq_result:
                for key, value in yq.items():
                    if key == "equals":
                        flag = self.equals_assert(yq, sj_result, result_code)
                        all_flag = all_flag + flag
                    elif key == "contains":
                        flag = self.contains_assert(value, sj_result)
                        all_flag = all_flag + flag
                    else:
                        print("框架暂不支持此断言方式")
            assert all_flag == 0
            logs("接口测试成功")
            logs("--------接口测试结束--------\n\n")
        except Exception:
            logs("接口测试失败")
            logs("--------接口测试结束--------\n\n")
            error_log("断言assert_result异常：%s" % str(traceback.format_exc()))

    # 相等断言
    def equals_assert(self, value, sj_result, result_code):
        flag = 0

        for assert_key, assert_value in value.items():
            if assert_key == "status_code":
                if assert_value != result_code:
                    flag = flag + 1
                    print("断言失败：返回的状态码不等于%s" % assert_value)
            else:
                lists = jsonpath.jsonpath(sj_result, '$..promptText')
                if lists:
                    if isinstance(assert_value, str):
                        if assert_value not in lists:
                            flag = flag + 1
                            print("断言失败:" + "promptText字段" + "不等于：" + str(assert_value))
                            print(f'返回结果为：{sj_result}')
                    if isinstance(assert_value, dict):
                        robot = read_config("system", "robot")
                        if assert_value[str(robot)] not in lists:
                            flag = flag + 1
                            print("断言失败:" + "promptText字段" + "不等于：" + str(assert_value[str(robot)]))
                            print(f'返回结果为：{sj_result}')
                else:
                    flag = flag + 1
                    print("断言失败:返回的结果中不存在:" + assert_value)
            return flag

    # 包含断言
    def contains_assert(self, value, sj_result):
        flag = 0
        if str(value) not in str(sj_result):
            flag = flag + 1
            print("断言失败:返回的结果中不包含：" + value)
        return flag


if __name__ == '__main__':
    pass
