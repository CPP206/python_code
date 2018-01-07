# -*- coding: utf-8 -*-
import scrapy
import urllib
from dongguan.items import DongguanItem

class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0768.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='

    # url = url + urllib.urlencode(param)

    headers = {
    	"User-Agent" : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    	'Host' : 'wz.sun0769.com',
    }
 
    # 使用下面的start_requests好像没办法使翻页的这种请求参数递增
    def start_requests(self):
    	return [scrapy.Request(url = self.url, callback = self.parse)]
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
    	#取出每一页中每个帖子链接列表
    	links = response.xpath('//div[@class="greyframe"]//tr/td/a[@class="news14"]/@href').extract()
        for link in links:
        	print(link)
        	yield scrapy.Request(link, headers=self.headers, callback=self.parse_item)
        #提取下一页链接
        next_page = response.xpath('//div[@class="pagination"]/a[text()=">"]/@href')
        
        if next_page is not None:
        	print(next_page.extract()[0])
        	yield scrapy.Request(next_page.extract()[0], callback = self.parse)

    #处理每个帖子
    def parse_item(self, response):
    	print("******************************test*******************************")
    	item = DongguanItem()
    	#标题
    	item['title'] = response.xpath('//head/title').extract()[0]
    	print(item['title'])

    	yield item

