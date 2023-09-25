# -*- coding: utf-8 -*-

from websocket import create_connection
import json

url = "ws://10.168.47.14:6688/queue/join"
ws = create_connection(url)

ws.send('{"fn_index":2,"session_hash":"gbi9kzewj1v"}')
ws.send('{"fn_index":2,"data":["介绍一下天籁",null,null,[],null,null,null],"event_data":null,"session_hash":"gbi9kzewj1v"}')
res = ws.recv()
print(res)

while json.loads(res)["msg"] != "process_completed":
    res = ws.recv()
    print(json.loads(res, encoding="utf-8"))
print("done")
