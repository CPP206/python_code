#-*- coding:utf-8 -*-
from scrapy import Spider, Request, FormRequest

class GithubLoginSpider(Spider):
	name = "github"
	allow_domains = ['github.com']

	#post登入必须的头字段
	post_headers = {
		# "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
		# "Referer" : "https://github.com",
		# "Origin" : 'https://github.com',
		# "Host":'github.com'
	}

	def start_requests(self):
		"""
			执行spider请求
			：return 返回一个Request对象，请求登陆的页面
		"""
		return [Request(url="https://github.com/login", meta={"cookiejar":1}, callback = self.post_login, headers = self.post_headers)]

	def post_login(self, response):
		"""
			登陆的页面请求成功后，解析响应的页面，获取登陆需要的<input>标签信息
			:param response :登陆接口返回的页面
		"""

		#github登陆上传必要的字段
		utf8 = response.xpath('//form//input[@name="utf8"]/@value').extract()[0]
		authenticity_token = response.xpath('//form//input[@name="authenticity_token"]/@value').extract()[0]
		login = "1216938752@qq.com"
		password = "chenqi1992"
		commit = response.xpath('//form//input[@name="commit"]/@value').extract()[0]

		#发送FormRequest表单请求
		return FormRequest.from_response(response=response, meta={"cookiejar":response.meta['cookiejar']},
			formdata = {
				"utf8" : utf8,
				"authenticity_token" :authenticity_token,
				"login" : login,
				"password" : password,
				"commit" : commit
			},
			callback = self.after_login,
			headers = self.post_headers
			)

	def after_login(self, response):
		"""
			form表单请求成功后，请求登陆我的页面
			：param response
			:return:返回一个响应
		"""
		print(response.body)
		if response.status == 200:
			with open("my_github.html", "wb") as f:
				f.write(response.body)