#-*- coding:utf-8 -*-
#neihan.py

"""
	本篇主要就是使用re正则表达式来解析正则表达式
"""
import random
import urllib2
import requests
import re

#定义handler处理器
handler = urllib2.ProxyHandler()

#定义一个opener
opener = urllib2.build_opener(handler)

#安装opener，可以全局使用urllib2.open()
urllib2.install_opener(opener)

#加入请求头，User-Agent
headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}

#请求地址
url = "http://www.neihan8.com/article/index_2.html"

#定义一个request
request = urllib2.Request(url=url, headers=headers)

#请求一个重定向
request.add_header('Referer', "http://www.neihan8.com/article/")

response = opener.open(request)

html = response.read()

pattern = re.compile(r'<div.*?class="column-title box box-790">(.*)?</div>', re.S)

item_list = pattern.findall(html)

for item in item_list:
	print(item)