# -*- coding:utf-8 -*-

import socket
import time
import threading


def udplink(sock, data, addr):
	print("Received from %s:%s" % addr)
	reply = 'Hello,%s!' % data.decode('utf-8')
	time.sleep(1)
	sock.sendto(reply.encode('utf-8'), addr)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

while True:
	data, addr = s.recvfrom(1024)
	threading.Thread(target=udplink, args=(s, data, addr))


