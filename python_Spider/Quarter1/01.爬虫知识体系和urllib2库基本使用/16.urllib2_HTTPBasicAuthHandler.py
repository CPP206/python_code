# -*- coding:utf-8 -*-
import urllib
import urllib2

#用户名
user = "test"

#密码
passwd = "123456"

＃web服务器IP
webserver = "18.123.123.1:16354"

#1. 构建一个用户密码管理对象，用来保存需要处理的用户密码
passmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

#2. 添加账户信息，第一个参数是realm与远程服务器相关的域消息，一般没人管都是写None,后面三个参数分别是服务器，用户名，密码
passmgr.add_password(None, webserver, user, passwd)

#3.构建一个Http基础用户名/密码验证的HTTPBasicAuthHandler处理器对象，参数是创建的密码管理对象
httpauth_handler = urllib2.HTTPBasicAuthHandler(passmgr)

#4.通过build_opener()方法使用这些代理handler对象，创建自定义的opener对象，参数是创建的httpauth_handler
opener = urllib2.build_opener(httpauth_handler)

#5.可以选择通过install_opener()方法定义全局opener
urllib2.install_opener(opener)

#6.构建request对象
request = urllib2.Request("http://www.baidu.com/")

#7.定义opener为全局opener后，可直接使用urlopen()请求
response = urllib2.urlopen(request)

#8.打印回应
print(response.read())

