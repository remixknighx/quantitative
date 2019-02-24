# -*- coding: utf-8 -*-
import socket

# 实例初始化
client = socket.socket()
# 访问服务器的ip和端口
ip_port = ("127.0.0.1", 8888)
# 连接主机
client.connect(ip_port)
# 定义一个循环，不断的发送消息
while True:
    # 接受主机信息
    data = client.recv(1024)
    # 打印接收的数据
    print(data.decode())
    # 输入发送的消息
    msg_input = input("请输入发送的消息: ")
    # 消息发送
    client.send(msg_input.encode())
    if msg_input == 'exit':
        break
    # 接受主机信息
    data = client.recv(1024)
    # 打印接收的数据
    print(data.decode())
