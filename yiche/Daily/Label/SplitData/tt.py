# -*- coding: utf-8 -*-

import json

data1 = []
data2 = []
with open('./data.json', 'r') as f:
    data = json.load(f)
    for i in range(len(data)):
        if i <len(data)/2:
          data1.append(data[i])
        else:
            data2.append(data[i])
print(len(data1))
print(len(data2))
with open('./data1', 'w') as f:
    f.write(str(data1))
with open('./data2', 'w') as f:
    f.write(str(data2))

