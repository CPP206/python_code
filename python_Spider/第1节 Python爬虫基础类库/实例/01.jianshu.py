#-*- coding:utf-8 -*-
#jianshu.py


import urllib2
import urllib
import cookielib
import random
import os


#自定义CookieJar
cookiejar = cookielib.LWPCookieJar("cookie.txt")
cookiehandler = urllib2.HTTPCookieProcessor(cookiejar)

opener = urllib2.build_opener(cookiehandler)

urllib2.install_opener(opener)
opener.addheaders = [("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]

headers = {
	"Accept":"application/json",
	"Accept-Language":"zh-CN,zh;q=0.8",
	"Connection":"keep-alive",
	"Cookie":"read_mode=day; default_font=font2; remember_user_token=W1sxOTM2NDA1XSwiJDJhJDEwJDhHTXA1cDd5STduSGFDc3piaVY2R3UiLCIxNTExMjYyMTkxLjA0MDczNTciXQ%3D%3D--e5b62aabe1dcbbe6292fbc54108e1bfc9740f856; locale=zh-CN; _m7e_session=3f5edcc56b82b61b1e2716b19aba1e37; _ga=GA1.2.392572307.1511059258; _gid=GA1.2.1033490030.1511262111; _gat=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221936405%22%2C%22%24device_id%22%3A%2215fd2267a10124-064e9e861630a5-6b1b1279-1049088-15fd2267a1151a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2215fd2267a10124-064e9e861630a5-6b1b1279-1049088-15fd2267a1151a%22%7D; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1511091526,1511262111,1511262125,1511262188; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1511262661",
	'If-None-Match':'W/"2844ec55a8529dcda24d6fe03cf020c4"',
	'Referer':'http://www.jianshu.com/'
}

request = urllib2.Request("http://www.jianshu.com/notifications?type=others&page=1", headers = headers)

request.add_header('Host', 'www.jianshu.com')


response = urllib2.urlopen(request)
print(response.read())

