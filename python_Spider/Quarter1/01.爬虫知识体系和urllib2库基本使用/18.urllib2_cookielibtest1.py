#-*- coding:utf-8 -*-
#18.urllib2_cookielibtest1.py

import cookielib
import urllib2

#构建一个CookieJar对象实力来保存cookie
cookiejar = cookielib.CookieJar()

#使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = urllib2.HTTPCookieProcessor(cookiejar)

#通过build_opener()来构建opener
opener = urllib2.build_opener(handler)

#以get方式访问页面，访问之后会自动保存cookie到cookiejar中
opener.open("http://www.baidu.com")

###可以按照标准格式将保存的cookie打印出来
cookieStr = ""

for item in cookiejar:
	cookieStr = cookieStr + item.name + "=" +item.value+";" 

##舍去最后一位的分号
print(cookieStr[:-1])