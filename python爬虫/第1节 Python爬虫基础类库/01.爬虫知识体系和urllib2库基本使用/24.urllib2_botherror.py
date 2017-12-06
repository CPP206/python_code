#-*- coding:utf-8 -*-
#24.urllib2_botherror.py

import urllib2

request = urllib2.Request("http://blog.baidu.com/itcast")

try:
    urllib2.urlopen(request)
except urllib2.HTTPError,err:
    print err.code
except urllib2.URLError,err:
    print err

else:
    print "Good Job"