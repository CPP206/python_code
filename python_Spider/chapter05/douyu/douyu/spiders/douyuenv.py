# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem

class DouyuenvSpider(scrapy.Spider):
    name = 'douyuenv'
    allowed_domains = ['capi.douyu.cn']
    
    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="

    start_urls = [url + str(offset)]

    def parse(self, response):
        # print("起始地址： %s"%(self.start_urls))
        #把json格式的数据转换为python，data段是列表
        data = json.loads(response.text)["data"]
        for each in data:
        	item = DouyuItem()
        	#获取房间播主
        	item['nickname'] = each["nickname"]  
        	#获取头像链接
        	item['imagelink'] = each['vertical_src']
        	yield item
     
        self.offset += 20
        print(self.url + str(self.offset))
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)