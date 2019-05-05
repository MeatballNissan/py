import socket


# socket.TCP/IP  协议类型 -地址簇
#socket.SOCK_STREAM (TCP)
#socket.SOCK_DGRAM(UDP)
#洪水攻击  通过不断伪造ip去请求服务，socket.SOCK_RAW可以伪造ip头
#两个进程默认不能通讯，但是可以通过socket
client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(("localhost",6099))

while True:
    msg = input("》》：").strip()
    client.send(msg.encode("utf-8"))
    data= client.recv(1024)
    print(data.decode())
    print(type(data))

client.close()