#-*- coding:utf-8 -*-
#20.urllib2_cookielibtest3.py

import cookielib
import urllib2

# 创建MozillaCookieJar(有load实现)实例对象
cookiejar = cookielib.MozillaCookieJar()

# 从文件中读取cookie内容到变量
cookiejar.load("test.txt")

#使用HTTPCookieProcessor()来创建cookie处理器对象，参数为cookiejar
handler = urllib2.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = urllib2.build_opener(handler)

request = urllib2.Request("http://www.baidu.com")

response = opener.open(request)

print(response.read())