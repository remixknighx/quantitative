# -*- coding: utf-8 -*-

import socket
import random

# 创建实例
sk = socket.socket()
# 定义绑定ip和port
ip_port = ("127.0.0.1", 8888)
# 绑定监听
sk.bind(ip_port)
# 最大连接数，可以挂起的最大连接数为5，拒绝第6个请求
sk.listen(5)
while True:
    # 提示信息
    print("正在进行等待接收数据.....")
    # 接受数据
    conn, address = sk.accept()
    # 定义信息
    msg = "连接成功"
    # 返回信息
    conn.send(msg.encode())
    # 不断接受客户端发来的消息
    while True:
        # 接受客户端消息
        data = conn.recv(1024)
        # 打印数据
        print(data.decode())
        # 接收到退出指令
        if data == b'exit':
            break
        # 处理客户端消息
        conn.send(data)
        # 发送随机数信息
        conn.send(str(random.randint(1, 1000)).encode())
    # 主动关闭连接
    conn.close()


"""
Socket参数
family: 地址簇
    socket.AF_INET IPV4(默认)
    socket.AF_INET6 IPV6
    socket.AF_UNIX只能够用于单一的UNIT系统进程间通信
    
type：类型
    socket.SOCK_STREAM 流式socket, for TCP（默认）
    socket.SOCK_DGRAM  数据报式socket, for UDP
    socket.SOCK_RAW    原始套接字（使用较少）
    socket.SOCK_RDM    可靠UDP形式（UDP进行数据校验，使用较少）
    socket.SOCK_SEQPACKET  可靠的连续数据包服务
    
proto：协议号
    0: 默认，可以省略
    CAN_RAW或CAN_BCM：地址簇为AF_CAN时
"""
