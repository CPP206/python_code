#-*-  coding:utf-8 -*- 


import urllib2

# 代理有用户密码的就会报407错误
authproxy_handle = urllib2.ProxyHandler({"http":"114.215.104.49.16816"})
opener = urllib2.build_opener(authproxy_handle)

request = urllib2.Request("http://www.baidu.com")

urllib2.install_opener(opener)

urllib2.urlopen(request)