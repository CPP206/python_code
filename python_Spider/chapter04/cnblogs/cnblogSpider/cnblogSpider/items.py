# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()


class TencentItem(scrapy.Item):
	name = scrapy.Field()
	detailLink = scrapy.Field()
	positionInfo = scrapy.Field()
	peopleNumber = scrapy.Field()
	workLocation = scrapy.Field()
	publishTime = scrapy.Field()


class SaveGirlImageItem(scrapy.Item):
	name = scrapy.Field()
	url = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()
