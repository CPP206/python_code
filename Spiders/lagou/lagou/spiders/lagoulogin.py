# -*- coding: utf-8 -*-
import scrapy


class LagouloginSpider(scrapy.Spider):
    name = 'lagoulogin'
    allowed_domains = ['www.lagou.com']

    headers = {
    	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    	'Host' : 'passport.lagou.com'
    }

    def start_requests(self):
    	url = 'https://passport.lagou.com/login/login.html'

    	yield scrapy.Request(url=url, headers = self.headers, callback = self.parse)

    def parse(self, response):
        return scrapy.FormRequest.from_response(
        		response, formdata = {'username' : '1216938752@qq.com', 'password' : 'chenqi1992', 'isValidate' : 'true'},
        		callback = self.after_login
        	)

    def after_login(self, response):
    	print(response.body)
