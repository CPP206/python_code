#-*-  coding:utf-8 -*-

import urllib2
import re

class Spider:
	def __init__(self):
		pass

	def loadPage(sele, page):
		"""
			作用：下载页面

		"""
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
			"Cookie" : r'uuid="w:46316e2bec6e4f478353c2136e667c85"; tt_webid=6485884760606705166; login_flag=51b444667f078a55936fdb0a9310cb2d; sessionid=5cd6d6a965c4a25469a6154dbdbd8d57; uid_tt=35e458e9e92a513bc1669895018650eb; sid_tt=5cd6d6a965c4a25469a6154dbdbd8d57; sid_guard="5cd6d6a965c4a25469a6154dbdbd8d57|1510112814|15552000|Mon\054 07-May-2018 03:46:54 GMT"; csrftoken=dbd0673234833c7f04d8629258bfd080; _ga=GA1.2.1865933211.1510112749; _gid=GA1.2.649978839.1510112749',
			'Refer' : 'http://neihanshequ.com/user/4702280546/publish/'
		}	

		request = urllib2.Request('http://neihanshequ.com/', headers = headers)
		httpHandler = urllib2.HTTPHandler()


		opener = urllib2.build_opener(httpHandler)

		urllib2.install_opener(opener)

		response = urllib2.urlopen(request)
		f = open(u'内涵.html', 'w+')
		print(response.read())
		# f.write(response.read())
		# f.close()

if __name__ == "__main__":
	spider = Spider()
	spider.loadPage(2)
