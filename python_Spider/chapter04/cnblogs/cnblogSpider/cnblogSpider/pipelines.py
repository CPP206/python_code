# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CnblogspiderPipeline(object):

    def process_item(self, item, spider):
    	print("CnblogspiderPipeline")
        return item


class CnblogspiderPipeline2(object):

    def process_item(self, item, spider):
    	print("CnblogspiderPipeline22222")
        return item