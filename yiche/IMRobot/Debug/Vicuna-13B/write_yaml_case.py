# -*- coding: utf-8 -*-

import yaml
import json

# json转yaml
with open('./case_0705.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    with open('./case.yaml', 'a', encoding='utf-8') as ff:
        yaml.dump(data=data, stream=ff, allow_unicode=True, sort_keys=False)




