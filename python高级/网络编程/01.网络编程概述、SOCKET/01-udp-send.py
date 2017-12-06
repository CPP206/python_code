from socket import *

udpsocket = socket(AF_INET, SOCK_DGRAM)
#使用udp发送数据，在每一次的都需要接收方的ip和port
udpsocket.sendto(b"haha",('192.168.123.121', 8080))