# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#使用图片管道下载图片，但是默认的图片下载名称是无法更改的，所以要重写ImagesPipeline的方法

import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os


class ImagesPipeline(ImagesPipeline):
	#获取settings文件里设置的变量值
	IMAGES_STORE = get_project_settings().get("IMAGES_STORE")


	#默认是读取item里面的IMAGES_URLS_FIELD字段，如果不重写的话，如果使用内置图片下载方式要把图片链接放到IMAGES_URLS_FIELD字段里面
	def get_media_requests(self, item, info):
		image_url = item['imagelink']
		yield scrapy.Request(image_url)

	def item_completed(self, result, item, info):
		#这句话是固定写法,每次只返回一个image_path组成的列表，故每次只取0就可以了
		image_path = [x["path"] for ok, x in result if ok]
		print("图片地址： %s"%image_path)


		#下面这句话是更改图片的名称，也就是每个item下载完成以后，马上就更改下载的图片名称
		os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item['nickname'] + ".jpg")

		#这里把下载的图片绝对地址赋值给item
		item['imagePath'] = self.IMAGES_STORE + "/" + item['nickname']
		return item

class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item
