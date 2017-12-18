#-*- coding:utf-8 -*-
#02.urllib2_request.py

import urllib2

#url作为Request()方法的参数，构造并返回一个Request对象
request = urllib2.Request("http://www.baidu.com")

#Request对象作为一个urlopen()方法的参数，发送给服务器并接收响应
response = urllib2.urlopen(request)

html = response.read()

print(html)