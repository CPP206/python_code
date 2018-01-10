# -*- coding: utf-8 -*-
import scrapy
from sina.items import SinaItem
import os


class SinanewSpider(scrapy.Spider):
    name = 'sinanew'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
    	items = []

    	#获取所有大类的名称
        parentTitle = response.xpath('//div[@id="tab01"]//div//h3/a/text()').extract()
        #获取所有大类的链接
        parentUrls = response.xpath('//div[@id="tab01"]//div//h3/a/@href').extract()

        #获取所有小类的url和标题
        subUrls = response.xpath('//div[@id="tab01"]//div//ul/li/a/@href').extract()
        #获取所有小类的名称
        subTitle = response.xpath('//div[@id="tab01"]//div//ul/li/a/text()').extract()
        #爬取所有大类
        for i in range(0, len(parentTitle)):

        	item = SinaItem()

        	#指定打猎目录的路径和目录名
        	paraentFilename = "./Data/" + parentTitle[i]

        	#如果目录不存在，则创建目录
        	if(not os.path.exists(paraentFilename)):
        		os.makedirs(paraentFilename)

        	#爬取所有小类
        	for j in range(0, len(subUrls)):
        		item = SinaItem()

        		#保存大类的title和urls
        		item['parentTitle'] = parentTitle[i]
        		item['parentUrls'] = parentUrls[i]

        		#检查小类的url是否已同类别大类url开头，如果是返回True(sports.sina.com.cn和sports.sina.com.cn/nba)

        		if subUrls[j].startswith(item['parentUrls']):
        			subFilename = paraentFilename + '/' + subTitle[j]
        			print(subFilename)
        			#如果目录不存在，则创建目录
        			if(not os.path.exists(subFilename)):
        				os.makedirs(subFilename)

        			#存储小类url、title和filename字段数据
        			item['subUrls'] = subUrls[j]
        			item['subTitle'] = subTitle[j]
        			item['subFilename'] = subFilename

        			items.append(item)

        #发送每个小类url的Request请求，得到Response连同包含meta数据一同交给回调函数，second_parse方法处理

        for item in items:
        	yield scrapy.Request(url = item['subUrls'], meta = {'meta_1' : item}, callback = self.second_parse)

    #对于返回的小类url，再进行递归请求
    def second_parse(self, response):
    	#提取每次Response的meta数据
    	meta_1 = response.meta['meta_1']

    	#取出小类里的所有链接
    	sonUrls = response.xpath('//a/@href').extract()

    	items = []
    	for i in range(0, len(sonUrls)):
    		if sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls']):
    			item = SinaItem()
    			item['parentUrls'] = meta_1['parentUrls']
    			item['parentTitle'] = meta_1['parentTitle']
    			item['subUrls'] = meta_1['subUrls']
    			item['subTitle'] = meta_1['subTitle']
    			item['subFilename'] = meta_1['subFilename']
    			item['sonUrls'] = sonUrls[i]

    			items.append(item)

    	#发送每个小类子链接url的Request请求，得到Response后连同包含meta数据一同交给回调函数detail_parse
    	for item in items:
    		yield scrapy.Request(url=item['sonUrls'], meta = {'meta_2':item}, callback = self.detail_parse)

    def detail_parse(self, response):
    	item = response.meta['meta_2']
    	content = ""
    	head = response.xpath('//h1[@class="main-title"]/text()').extract()

    	content_list = response.xpath('//div[@id="article"]/p/text()').extract()
    	for content_one in content_list:
    		content += content_one
    	item['head'] = head
    	item['content'] = content

    	yield item