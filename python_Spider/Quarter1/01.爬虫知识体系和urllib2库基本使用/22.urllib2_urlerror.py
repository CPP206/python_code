#-*- coding:utf-8 -*-
# urllib2_urlerror.py

import urllib2

request = urllib2.Request('http://www.ajkfhafwjqh.com')


try:
    urllib2.urlopen(request, timeout=5)
except urllib2.URLError, err:
    print err