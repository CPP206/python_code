# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
	#帖子标题
	title = scrapy.Field()
	#帖子编号
	number = scrapy.Field()
	#帖子内容
	content = scrapy.Field()
	#帖子状态
	status = scrapy.Field()
	#帖子发表者 网友
	net_friend = scrapy.Field()
	#时间
	time = scrapy.Field()