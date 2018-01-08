# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 文件处理类库，可以指定编码格式
import codecs
import json


class JsonWritePipeline(object):

    def __init__(self):
        # 创建一个文件，指定格式为utf-8
        self.filename = codecs.open('sunwz.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(content)
        return item

    def spider_close(self, spider):
        print("爬虫结束")
        self.file.close()


class DongguanPipeline(object):

    def process_item(self, item, spider):
        return item
