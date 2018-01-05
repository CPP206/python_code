#-*- coding:utf-8 -*-

import scrapy
import json
from mySpider.items import DouyuspiderItem


class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["http://capi.douyucdn.cn"]

    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    strt_urls = url + str(offset)

    def parse(self, response):
        #返回从json里获取data端数据集合
        pass