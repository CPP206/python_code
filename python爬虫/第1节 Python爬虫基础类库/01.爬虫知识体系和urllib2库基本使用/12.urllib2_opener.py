#-*- coding:utf-8 -*-
#12.urllib2_opener.py

import urllib2

#构建一个HTTPHandler处理器
http_handler = urllib2.HTTPHandler();

#调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener
opener = urllib2.build_opener(http_handler)

#构建Request请求
request = urllib2.Request("http://www.baidu.com")

#调用自定义的opener对象的open()方法，发送request请求
response = opener.open(request)

#获取服务器响应内容
print(response.read())