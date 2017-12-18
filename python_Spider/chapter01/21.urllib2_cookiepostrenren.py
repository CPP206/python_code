#-*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib

#构建一个CookieJar对象实例来保存cookie
cookiejar = cookielib.CookieJar()

proxthandler = urllib2.HTTPCookieProcessor(cookiejar)

opener = urllib2.build_opener(proxthandler)

opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

data = {"email":"1216938752@qq.com", "password":"chenqi1992"}

postdata = urllib.urlencode(data)

request = urllib2.Request("http://www.renren.com/PLogin.do", data = postdata)

response = opener.open("http://www.renren.com/410043129/profile")

print(response.read())