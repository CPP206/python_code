# -*- coding: utf-8 -*-
import scrapy
from cnblogSpider.items import CnblogspiderItem

class CnblogSpider(scrapy.Spider):
    name = 'cnblog'
    allowed_domains = ['www.cnblogs.com']
    start_urls= ["http://www.cnblogs.com/miqi1992/default.html?page=2"]

    def parse(self, response):
	    # print(response.body)
	    # filename = "cnblog.html"
	    # with open(filename, 'w') as f:
	    #     f.write(response.body)

	    #存放博客的集合
	    items = []

	    for each in response.xpath(".//*[@class='day']"):
	    	item = CnblogspiderItem()
	    	url = each.xpath('.//*[@class="postTitle"]/a/@href').extract()[0]
	    	title = each.xpath('.//*[@class="postTitle"]/a/text()').extract()[0]
	    	time = each.xpath('.//*[@class="dayTitle"]/a/text()').extract()[0]
	    	content = each.xpath('.//*[@class="postCon"]/div/text()').extract()[0]

	    	item['url'] = url
	    	item['title'] = title
	    	item['time'] = time
	    	item['content'] = content 
	    	
	    	# yield item

	    next_page = response.xpath(".//*[@id='homepage1_HomePageDays_homepage_bottom_pager']/div/a[last()]/@href").extract()[0]
	    if next_page:
	    	yield scrapy.Request(url=next_page, callback=self.parse)
	    	# items.append(item)

	    #直接返回最后数据
	    # return items
