#-*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import Request
import logging
import re
from cnblogSpider.items import SaveGirlImageItem

logger = logging.getLogger(__name__)

class MeiziTuSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ['meizitu.com']
    user_header = {
        "Referer": "http://www.meizitu.com/tag/nvshen_460_1.html",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0"
    }

    def start_requests(self):
        logging.debug("###### 妹子图Spider开始启动.....%s"%self)
        return [Request(url="http://www.meizitu.com/tag/nvshen_460_1.html", callback=self.parse, headers = self.user_header)]

    @staticmethod
    def __remove_html_tags(str):
        return re.sub(r'<[^>]+>', '', str)


    def parse(self, response):
        # print(response.body)
        for picdiv in response.css('div[class="pic"]'):
            image_urls = picdiv.css('a[target="_blank"] img::attr(src)').extract_first()
            image_split = image_urls.split("/")
            image_name = image_split[-3]+ image_split[-2]+ image_split[-1]
            yield SaveGirlImageItem({
                'name' : MeiziTuSpider.__remove_html_tags(picdiv.css('a[target="_blank"] img::attr(alt)').extract()[0]),#获取这组相片的名称
                'url' : picdiv.css('a[target="_blank"] img::attr(src)').extract_first(),  #获取这组照片的链接
                'image_urls' : [picdiv.css('a[target="_blank"] img::attr(src)').extract_first()],
                'images' : image_name
            })

        next_page = response.xpath(u'//div[@class="navigation"]//li/a[contains(.,"下一页")]/@href').extract_first()

        if next_page is not None:
            requesturl = "http://www.meizitu.com" + next_page
            yield Request(requesturl, callback = self.parse, headers=self.user_header)

