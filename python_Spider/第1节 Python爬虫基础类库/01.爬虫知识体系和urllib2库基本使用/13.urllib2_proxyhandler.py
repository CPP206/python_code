#-*- coding:utf-8 -*-
#urllib2_proxyhandler.py


import urllib2

#构建了两个代理Handler,一个有代理IP,一个没有代理IP
httpproxy_handler = urllib2.ProxyHandler({"http":"120.76.55.49:8088"})
nullproxy_handler = urllib2.ProxyHandler({})

proxyswitch = True   #定义一个代理开关


#通过urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener

if proxyswitch:
	opener = urllib2.build_opener(httpproxy_handler)
else:
	opener = urllib2.build_opener(nullproxy_handler)

request = urllib2.Request("http://www.baidu.com/")

#1.如果这么写，只有使用opener.open()方法发送请才使用自定义的代理，而urlopen()使用自定义代理
response = opener.open(request)

#2.如果这么写，就是opener应用到全局，之后所有的，不管是opener.open()还是urlopen()发送请求，都将使用自定义代理
# urllib2.install_opener(opener)
# response = urllib2.urlopen(request)

print(response.read())