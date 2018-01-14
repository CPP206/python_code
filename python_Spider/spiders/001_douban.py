#-*-  coding:utf-8 -*-
import urllib2
import urllib
import re
import requests
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

for a in range(10):
	url = 'https://book.douban.com/top250?start={page}'.format(page=a*25)
	print("开始下载第 {page} 页。。。。。。".format(page=a+1))


	response = requests.get(url = url)
	print(response.json)

	request = urllib2.Request(url)

	response = urllib2.urlopen(request)

	s = etree.HTML(response.read())

	file = s.xpath('//div[@id="wrapper"]//div[contains(@class,"article")]//table')

	# print(file)

	for book in file:
		#图片链接
		image_url = book.xpath('./tr/td/a/img/@src')[0]
		#书名
		title = book.xpath('./tr/td[last()]/div/a/@title')[0]
		#评分
		score = book.xpath('./tr/td[last()]/div/span[last()-1]/text()')[0]
		#书籍链接
		url = book.xpath('./tr/td[last()]/div/a/@href')[0]
		#评价人数
		num = book.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip("(").strip(")").strip()
		print("********************************************")
		print('{name}\n{score}\n{num}\n{url}\n{image_url}'.format(name=title, score=score,num = num, url = url, image_url=image_url))
	print("。。。。。。。第 {page} 页下载结束".format(page=a + 1))