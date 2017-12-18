#-*- coding:utf-8 -*-
#23.urllib2_urllib2_httperror.py

import urllib2

request = urllib2.Request("http://blog.baidu.com/itcast")  

try:
    urllib2.urlopen(request)
except urllib2.HTTPError, err:
    print err.code
    print err