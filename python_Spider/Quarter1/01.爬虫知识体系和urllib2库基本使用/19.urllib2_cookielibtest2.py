#-*- coding:utf-8 -*-
#19.urllib2_cookielibtest2.py

import cookielib
import urllib2

#保存cookie的本地磁盘文件名
filename = "cookie.txt"

#声明一个MozillaCookieJar(有save实现)对象实例来保存cookie,之后写入文件
cookiejar = cookielib.MozillaCookieJar(filename)

#使用HTTPCookieProcessor()创建cookie处理器对象，参数为cookieJar()对象
handler = urllib2.HTTPCookieProcessor(cookiejar)

#通过build_opener()对象来构建opener
opener = build_opener(handler)

#创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")

#保存cookie到本地文件
cookiejar.save()