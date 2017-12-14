#-*- coding:utf-8 -*-
import urllib2
import os

proxyuser = os.environ.get("proxyuser")
proxypasswd = os.environ.get("proxypasswd")

proxy_handler = urllib2.ProxyHandler({"http":proxyuser+":"+proxypasswd+"@172.23.32.12:80"})

opener = urllib2.build_opener(proxy_handler)


urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com")

response = urllib2.urlopen(request)
print(response.read())