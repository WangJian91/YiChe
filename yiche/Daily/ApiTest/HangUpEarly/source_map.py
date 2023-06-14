# 对外业务ID映射
business_source = {
    "A999": "其他",  # base:未指定业务id
    "A001": "智能小易",
    # "A002": "智能工牌",
    "A003": "C端电销"
}

Type = {"BASE": "base",
        "B_BUSINESS": "A001",
        "C_BUSINESS": "A003"
        }

business_map = {
    "A003": {
        "0": {"其他": []},
        "1": {"关机": ["1"]},
        "2": {"停机": ["2"]},
        "3": {"暂停服务": ["3"]},
        "4": {"呼入限制": ["4", "10"]},
        "5": {"呼叫转移": ["5"]},
        "6": {"欠费": ["6"]},
        "7": {"网络忙": ["7"]},
        "8": {"空号": ["8"]},
        "9": {"正在通话中": ["9"]}
    },
    "A001": {
        "0": {"其他": []},
        "1": {"关机": ["1"]},
        "2": {"停机": ["2"]},
        "3": {"暂时无法接通": ["10"]},
        "4": {"空号": ["8"]},
        "5": {"正在通话": ["9"]},
        "6": {"转来电提醒": ["5"]}
    }
}

default_map_path = {
    "path": "/opt/tritonserver/call_cpu_process/analysis_call/Config/default_map.txt",
    # "path": "/c_models/call_cpu_process/analysis_call/Config/default_map.txt",

}
