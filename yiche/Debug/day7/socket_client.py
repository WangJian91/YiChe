__author__ = "Alex Li"
# 客户端
# -*-coding:utf-8-*-

import socket

client = socket.socket()  # 声明socket类型，同时生成socket连接对象
client.connect(('localhost', 6969))
count = 0
while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    else:
        client.send(msg.encode("utf-8"))
        data = client.recv(10240)
        print("recv:", data.decode())
        count += 1
        if count >= 10:
            break
client.close()
