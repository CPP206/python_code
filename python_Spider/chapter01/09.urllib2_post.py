#-*- coding:utf-8 -*-
#09.urllib2_post.py

import urllib
import urllib2

#POST请求的目标URL
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers = {"User-Agent":"Mozilla...."}

formate = {
	"type":"AUTO",
	"i":"i love python",
	"doctype":"json",
	"xmlVersion":"1.8",
	"keyform":"fanyi.web",
	"ue":"utf-8",
	"action":"FY_BY_ENTER",
	"typoResult":"true"
}

data = urllib.urlencode(formate)

request = urllib2.Request(url, data=data, headers = headers)

response = urllib2.urlopen(request)


print("-"*30)
print(response.read())