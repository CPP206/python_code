#-*- coding:utf-8 -*-
#本篇将模拟执行javascript语句

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')