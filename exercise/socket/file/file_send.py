# -*- coding: utf-8 -*-
import socket

# 实例化模块
sk = socket.socket()
# 定义连接ip和port
ip_port = ('127.0.0.1', 6666)
# 服务器连接
sk.connect(ip_port)
# 文件上传
# 打开文件
with open('test.py', 'rb') as f:
    # 按每一段分割文件
    for i in f:
        # 数据上传
        sk.send(i)
        # 等待接收完成
        data = sk.recv(1024)
        # 判断服务器端是否真正的接收完成
        if data != b'success':
            break
# 给服务器端发送结束信号
sk.send('quit'.encode())
