#coding:utf-8
import urllib2

#构建一个HTTPHandleer处理器对象，支持处理Http请求

#在HTTPHandle增加 参数"debuglevel=1"将会自动打开debug log
http_handler = urllib2.HTTPHandler("debuglevel=1")

#调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = urllib2.build_opener(http_handler)

request = urllib2.Request("http://www.baidu.com")

response = opener.open(request)

# print(response.read())