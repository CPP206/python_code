# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import json


class FileJsonLine(object):

	JSON_FILE_PATH = get_project_settings().get('JSON_FILE_PATH')

	def __init__(self):
		if(not os.path.exists(self.JSON_FILE_PATH)):
			os.makedirs(self.JSON_FILE_PATH)
		print("----------------------------------------------")
		print(self.JSON_FILE_PATH + "" +"imooc.json")
		self.file = open(self.JSON_FILE_PATH +"/"+ "imooc.json", 'wb')

	def process_item(self, item, spider):
		print("json文件下载")
		course = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(course)
		return item
	def close_spider(self, spider):
		self.file.close()