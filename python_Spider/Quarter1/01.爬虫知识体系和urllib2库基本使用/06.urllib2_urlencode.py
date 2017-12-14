#-*- coding:utf-8 -*-
#06.urllib2_urlencode.py
import urllib2
import urllib

word = {"wd":"传智播客"}

#通过urllib.urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受
encode = urllib.urlencode(word)

print(encode)
#通过urllib.unquote()方法，把URL编码字符串，转换回原始字符串

print(urllib.unquote("wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2"))