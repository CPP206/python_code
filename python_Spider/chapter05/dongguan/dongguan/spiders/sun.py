# -*- coding: utf-8 -*-
import scrapy
import urllib
from dongguan.items import DongguanItem

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0768.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='

    # compile = re.
    # url = url + urllib.urlencode(param)

    headers = {
    	"User-Agent" : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    	'Host' : 'wz.sun0769.com',
    }
 
    # 使用下面的start_requests好像没办法使翻页的这种请求参数递增
    # def start_requests(self):
    # 	return [scrapy.Request(url = self.url, callback = self.parse)]
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
    	#取出每一页中每个帖子链接列表
    	links = response.xpath('//div[@class="greyframe"]//tr/td/a[@class="news14"]/@href').extract()
        for link in links:
        	print(link)
        	yield scrapy.Request(link, headers=self.headers, callback=self.parse_item, dont_filter=True)
        #提取下一页链接
        next_page = response.xpath('//div[@class="pagination"]/a[text()=">"]/@href')
        
        if next_page is not None:
        	print(next_page.extract()[0])
        	yield scrapy.Request(url = next_page.extract()[0], callback = self.parse, dont_filter=True)

    #处理每个帖子
    def parse_item(self, response):
    	item = DongguanItem()
    	#标题
    	item['title'] = response.xpath('//head/title/text()').extract()[0].replace('_阳光热线问政平台', "")

        #编号
        item['number'] = (response.xpath('//div[@class="pagecenter p3"]//strong//text()').extract()[0]).split(':')[-1]

        #帖子内容,默认取出有图片情况下的文字内容列表
        content = response.xpath('//div[@class="contentext"]/text()').extract()

        #如果没有图片，则取出没有图片情况下的文字内容列表
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()

        item['content'] = "".join(content).strip()
        
        #链接
        item['url'] = response.url

        #帖子状态
        item['status'] =  response.xpath('//div[@class="audit"]//span/text()').extract()[0]

        #网友
        item['net_friend'] = (response.xpath('//div[@class="cright"]//p//text()').extract()[0]).split("发言时间")[0].split("：")[1].strip()

        #时间
        item['time'] = (response.xpath('//div[@class="cright"]//p//text()').extract()[0]).split("发言时间")[1].strip()

    	yield item

