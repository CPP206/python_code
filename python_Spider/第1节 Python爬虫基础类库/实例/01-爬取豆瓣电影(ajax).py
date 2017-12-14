#-*- coding:utf-8 -*-
#主要爬取豆瓣电影里面分类，然后按剧情分类

import urllib
import urllib2

headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
formdata = {
	"type":"24",
	"action":"",
	"start":"60",
	"limit":"20"
}
url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action="

data = urllib.urlencode(formdata)
httpHandler = urllib2.HTTPHandler()
opener = urllib2.build_opener(httpHandler)
request = urllib2.Request(url = url)

response = opener.open(request)
print(response.read().decode("utf-8"))