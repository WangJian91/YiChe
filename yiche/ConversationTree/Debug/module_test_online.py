import pdb
import json
import requests
import base64

# host = "http://ai.uat.yixincapital.com/dcm/dcm"
# host = "http://ai.yxqiche.com/dcm/dcm/yxdcm"

# ports = [50000, 50020, 50021, 50022, 50023, 50024, 50025, 50026, 50027, 50028]
ports = [50000]

def get_robots(tenant_idx, robot_idx, inp):
    rbt = dict()
    rbt["name"] = str(tenant_idx) + "-" + str(robot_idx)
    rbt["tenant_idx"] = tenant_idx
    rbt["robot_idx"] = robot_idx
    rbt["inp"] = inp
    return rbt


robots = []
# robots.append(get_robots(2, 2077, ["你好", "你好", "嗯", "奔驰", "半年内", "易车", "易车"]))
# robots.append(get_robots(2, 2112, ["你好", "你好", "买的", "奔驰", "半年内", "易车", "易车"]))
# robots.append(get_robots(2, 31, ['你好', "不需要", "好的", "丰田", "卡罗拉", "南京", "对"]))
# robots.append(get_robots(2, 31, ['您好','你们是干什么的','是买车','丰田的卡罗拉']))

robots.append(get_robots(2, 2112, ["您好", "是的", "忙着呢", "有优惠吗", "你怎么知道我手机号的", "我不在北京"]))

# robots.append(get_robots(2, 22, ["没时间看", "你讲什么", "你好", "可以"]))
# robots.append(get_robots(2, 2112, ["你好", "不考虑", "男的多了老多地方了", "块收"]))
# robots.append(get_robots(2, 2112, ["你好", "不考虑", "男的多了老多地方了", "就算机车呀"]))
# robots.append(get_robots(2, 2112, ["你好", "不考虑", "男的多了老多地方了", "气质之交"]))
# robots.append(get_robots(2, 2112, ["你好", "不考虑", "男的多了老多地方了", "东撤第"]))
# robots.append(get_robots(2, 2112, ["你好", "不考虑", "男的多了老多地方了", "快搜"]))
# robots.append(get_robots(2, 2112, ["你好", "不考虑", "男的多了老多地方了", "没留过呀啥也没留过"]))
# robots.append(get_robots(2, 2112, ["你好", "不考虑", "男的多了老多地方了", "你们怎么天天打"]))
# robots.append(get_robots(2, 2112, ["你好", "不考虑", "男的多了老多地方了", "你打扰我了"]))


def test(port, name, tenant_idx, robot_idx, inp):
    host = "http://10.168.47.19:{}/algoplat/titan/engine/dcm/dcm/voicedcm".format(port)
    sessionIdx = "monitor_1313322212"

    post_data_init = {
        "sessionIdx": sessionIdx,
        "inAction": 1,
        "inParams": {
            "callIdx": sessionIdx,
            "tenantIdx": tenant_idx,
            "robotIdx": robot_idx,
            "env": 1,
            "userInfo": {
                "UserName": "旺德福",
                "Sex": "先生",
                "OrderNo": "订单号"
            }
        }
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(post_data_init)
    result = requests.post(host, data=json_data, headers=headers)
    json_result = result.json()
    print(name + "\t" + "promptText" + "\t" + str(json_result[0]['outParam']['promptText']))
    print(name + "\t" + "timeout" + "\t" + str(json_result[0]['outParam']['timeout']))

    # ba = base64.b64encode(open("../rela.m4a", "rb").read()).decode("utf-8")

    ft = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i, k in enumerate(inp):
        param_voice = {
            "callIdx": sessionIdx,
            "tenantIdx": tenant_idx,
            "robotIdx": robot_idx,
            "env": 1,
            "interIdx": 1,
            "beginPlay": "",
            "endPlay": "",
            "resultTime": "",
            "flowResultType": ft[i],  # 6 挂机  4 放音结束 # 3 系统异常,  # 2 按键 暂时不处理,  # 5 超时,  # 1 asr 文本
            "input": k,  # "000X",  # "1993年12月18日",  # "是的",
            "voiceType": "m4a"
        }

        post_data_voice = {
            "sessionIdx": sessionIdx,
            "inAction": 2,
            "inParams": param_voice,
        }
        headers = {'content-type': 'application/json'}
        json_data = json.dumps(post_data_voice)

        result = requests.post(host, data=json_data, headers=headers)
        json_result = result.json()
        print(result.request.body)
        # print(json_result)
        print(k)
        print(name + "\t" + "promptText" + "\t" + str(json_result[0]['outParam']['promptText']))
        print(name + "\t" + "timeout" + "\t" + str(json_result[0]['outParam']['timeout']))


for p in ports:
    for robot in robots:
        test(p, robot["name"], robot["tenant_idx"], robot["robot_idx"], robot["inp"])
