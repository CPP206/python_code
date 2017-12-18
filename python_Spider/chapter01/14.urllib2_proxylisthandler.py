#-*- coding:utf-8 -*-
#14.urllib2_proxylisthandler.py

import urllib2
import random

proxy_list = [
	{"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"}
]

#随机选择一个代理
proxy = random.choice(proxy_list)
#使用选择的代理创建一个代理处理器
proxy_handler = urllib2.ProxyHandler(proxy)

opener = urllib2.build_opener(proxy_handler)

urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com/")
response = opener.open(request)

print(response.read())