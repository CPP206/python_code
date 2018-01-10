# -*- coding: utf-8 -*-
import scrapy
from imook.items import ImookItem

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class ImooklistSpider(scrapy.Spider):

    name = 'imooklist'
    allowed_domains = ['www.imooc.com']
    start_urls = ['http://www.imooc.com/course/list']
    url = 'http://www.imooc.com'
    def parse(self, response):
        course_list = response.xpath('//div[@class="course-card-container"]/a/div/h3')
        items = []
        for i in range(0, len(course_list)):
        	item = ImookItem()
        	item['name'] = response.xpath('//div[@class="course-card-container"]/a/div/h3/text()').extract()[i]
        	item['number'] = response.xpath('//div[@class="course-card-container"]/a/div//div[contains(@class,"course-card-info")]/span[last()]/text()').extract()[i]
        	item['level'] = response.xpath('//div[@class="course-card-container"]/a/div//div[contains(@class,"course-card-info")]/span[1]/text()').extract()[i]
        	item['imgurl'] = "http:" + response.xpath('//div[@class="course-card-container"]//img/@src').extract()[i]
        	item['url'] = self.url + response.xpath('//div[@class="course-card-container"]/a/@href').extract()[i]
        	items.append(item)

        #再根据每个课程的url的request请求，得到Response连同包含meta数据，一同交给回调函数parse_course方法处理
        for item in items:
        	yield scrapy.Request(url = item['url'], meta = {'meta_1':item}, callback = self.parse_course)

        next_page = self.url + response.xpath(u'//div[@class="page"]/a[text()="下一页"]/@href').extract()[0]
        # yield scrapy.Request(url = next_page, callback = self.parse)

    def parse_course(self, response):
    	item = response.meta['meta_1']
    	item['longtime'] = response.xpath('//div[contains(@class,"statics")]/div[4]/span[@class="meta-value"]/text()').extract()[0]
    	item['score'] = response.xpath('//div[contains(@class,"statics")]/div[5]/span[@class="meta-value"]/text()').extract()[0]
    	item['content'] = response.xpath('//div[@class="course-brief"]/p/text()').extract()[0]


    	print("课程名称：%s"%(item['name']))
    	print("学习人数：%s"%(item['number']))
    	print("课程等级：%s"%(item['level']))
    	print("图片链接：%s"%(item['imgurl']))
    	print("读书时长%s" %(item['longtime']))
    	print('总和评分: %s'%(item['score']))
    	print("课程简介: %s"%(item['content']))

    	yield item


