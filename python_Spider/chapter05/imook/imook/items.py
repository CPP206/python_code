# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #课程名称
    name = scrapy.Field()
    #学习人数
    number = scrapy.Field()
    #课程难度
    level = scrapy.Field()
    #课程时长
    longtime = scrapy.Field()
    #总和评分
    score = scrapy.Field()
    #课程简介
    content = scrapy.Field()

    #图片链接
    imgurl = scrapy.Field()

    #课程地址
    url = scrapy.Field()

    #图片存储路径
    imagesPath = scrapy.Field()
