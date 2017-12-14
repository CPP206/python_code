#-*-  coding:utf-8 -*-
import urllib2
import urllib

import time


str = "战狼"
str2 = str.decode('gbk')

map = {"name":str2}
print(urllib.urlencode(map))