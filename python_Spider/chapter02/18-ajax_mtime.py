#-*-  coding:utf-8 -*-
import requests
import re
import time

class HtmlDownloader(object):
	def download(self, url, params=None):
		if url is None:
			return None
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'
		headers = {'User-Agent':user_agent}
		if params is None:
			r = requests.get(url, headers = headers)
		else:
			r = requests.get(url, headers = headers, params = params)
		if r.status_code == 200:
			r.encoding = 'utf-8'
			return r.text
		return None


class HtmlParser(object):
	def parser_url(self, page_url, response):
		pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
		urls = pattern.findall(response)
		if urls != None:
			#将urls去重
			return list(set(urls))
		else:
			return None

	def parse_json(self, page_url, response):
		"""
			解析响应
			:param response
			:return
		"""
		#将"="和";"之间的内容提取出来
		pattern = re.compile(r'=(.*?);')
		result = pattern.findall(response)[0]
		print(result)
		# if result != None:
		# 	#json模块加载字符串
		# 	value = json.loads(result)
		# 	try:
		# 		isRelease = value.get('value').get('isRelease')
		# 	except Exception, e:
		# 		print e
		# 		return None
		# 	if isRelease:
		# 		pass
				# if value.get('value').get('')






class SpiderMain(object):
	def __init__(self):
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()

	def crawl(self, root_url):
		content = self.downloader.download(root_url)
		urls = self.parser.parser_url(root_url, content)

		#构造一个活的评分和票房链接
		for url in urls:
			try:
				t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
				param = {
					'Ajax_CallBack':'true',
					'Ajax_CallBackType': 'Mtime.Library.Services',
					'Ajax_CallBackMethod': 'GetMovieOverviewRating',
					'Ajax_CallBackArgument0' : '%s'%(url[1]),
					'Ajax_RequestUrl' : '%s'%(url[0]),
					'Ajax_CrossDomain' : '1',
					't' : '%s'%t
				}
				rank_url = 'http://service.library.mtime.com/Movie.api?'
				rank_content = self.downloader.download(rank_url, param)
				data = self.parser.parse_json(rank_url, rank_content)

			except Exception, e:
				print("Crawl failed")

if __name__ == '__main__':
	spier = SpiderMain()
	spier.crawl('http://theater.mtime.com/China_Jiangsu_Province_Nanjing/')