#-*- coding:utf-8 -*-
#15.urllib2_proxy2.py

import urllib2
import urllib

#私密代理授权的账户
user = "mr_mao_hacker"
#私密代理授权的密码
passwd = "sffqry9r"

＃私密代理IP
proxyserver = "61.23.123.43:16813"

# 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()  

#2. 添加账户信息，第一个参数是realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 代理服务器,用户名，密码
passwdmgr.add_password(None, proxyserver, user, passwd)

#3. 构建一个基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
注意：这里不再使用普通的ProxyHandler累了。
proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)

#4. 通过build_opener()方法使用代理handler对象，创建自定义opener对象，参数包括构建的proxyauth_handler
opener = urllib2.build_opener(proxyauth_handler)

＃５．构建request请求
request = urllib2.Request("http://www.baidu.com/")

＃６．使用自定义的opener发送请求
response = opener.open(request)

＃７．打印响应内容
print(response.read())


