#-*- coding:utf-8 -*-
#urllib2_urlopen.py

#导入urllib2库

import urllib2

#向指定的url发送请求，并返回服务器的类文件对象
response = urllib2.urlopen("http://www.baidu.com")

#类文件对象支持文件对象的操作方法，如read()方法读取文件
html = response.read()

#打印字符串
print(html)