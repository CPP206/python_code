#导入webdriver
from selenium import webdriver

#要想调用按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://www.baidu.com/')

data = driver.find_element_by_id("wrapper").text

print(data)