#-*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

class douyuSelenium(unittest.TestCase):
	#初始化方法
	def setUp(self):
		self.driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

	#具体的测试用例方法，一定要以test开头
	def testDouyu(self):
		self.driver.get("http://www.douyu.com/directory/all")

		while True:
			#指定xml解析
			soup = BeautifulSoup(self.driver.page_source, "lxml")

			#返回当前页面的所有房间标题列表和观众人数列表
			titles = soup.find_all('h3' , {'class':"ellipsis"})
			print(len(titles))
			nums = soup.find_all('span', {'class': "dy-num fr"})

				# #使用zip()函数把列表合并，并创建一个远相对的列表[(1, 2), (3, 4)]
			for title, num in zip(nums, titles):
				print(u'观众人数： '+num.get_text().strip(), u'\t房间标题： '+title.get_text().strip())
			#page_source.find()未找到内容则返回-1
			if self.driver.page_source.find('shark-pager-disable-next') != -1:
				break
			self.driver.find_element_by_class_name('shark-pager-next').click()
			time.sleep(1)

	# 退出时的清理方法
	def tearDown(self):
		print("加载完成...")
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()