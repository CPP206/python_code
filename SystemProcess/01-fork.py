#-*- coding:utf-8 -*-

import os

#注意：fork函数，只在Unix/Linux/Mac上运行，window不可以

pid = os.fork()

if pid == 0:
	print("这个是子进程，子进程永远返回0")
	print("返回子进程的ID：{}".format(os.getpid()))
	print("返回父进程的id:{}".format(os.getppid()))
else:
	print("这个是主进程，返回的是子进程的ID")
	print("返回当前进程的ID：{}".format(os.getpid()))
