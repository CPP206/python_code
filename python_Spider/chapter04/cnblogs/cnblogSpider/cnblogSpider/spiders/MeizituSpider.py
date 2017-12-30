#-*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import Request
from scrapy import FormRequest   #FormRequest在scrapy.http包下面
import logging
from cnblogSpider.items import SaveGirlImageItem

logger = logging.getLogger(__name__)

class MeiziTuSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ['meizitu.com']

    def start_requests(self):
        logging.debug("###### 妹子图Spider开始启动.....%s"%self)
        return [scrapy.Request(url="http://www.meizitu.com/a/list_1_1.html", callback=self.parse)]

    @staticmethod
    def __remove_html_tags(str):
        return re.sub(r'<[^>]+>', '', str)


    def parse(self, response):
        for picdiv in response.css('div[class="pic"]'):
            yield SaveGirlImageItem({
                'name' : MeiziTuSpider.__remove_html_tags(picdiv.css('a[target="_blank"] img::attr(alt)').extract()[0]),
                'url' : picdiv.css('a[target="_blank"] img::attr(stc)').extract_first(),
                'image_urls' : [picdiv.css('a[target="_blank"] img::attr(src)').extract_first()]
            })

