#-*- coding:utf-8 -*-
import urllib2

#代理开关,表示是否启用代理
proxyswith = False

#构建一个Handle处理器对象，参数是一个字典类型，包括处理类型和代理服务器IP_PROT
httpproxy_handler = urllib2.ProxyHandler({"http" : "122.96.59.105:80"})

#构建一个没有代理的处理器对象
nullproxy_handler = urllib2.ProxyHandler({})

if proxyswith:
	opener = urllib2.build_opener(httpproxy_handler)
else:
	opener = urllib2.build_opener(nullproxy_handler)

#构建了一个全局的opener,之后所有的请求都可以用urlopen()方式去发送，也附带Handle的功能
urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com")

resposne = urllib2.urlopen(request)

print(resposne.read())