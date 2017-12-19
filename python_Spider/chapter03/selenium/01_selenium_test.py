#-*- coding:utf-8 -*-

# IPython2 测试代码

# 导入webdrier
from selenium import webdriver
import time


# 要想调用键盘按键操作需要引入key包
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()

# 如果没有在指定环境指定的PhantomJS位置
#driver = webdriver.PhantomJS(execuable_path="./phantjs")

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)
driver.get("http://www.baidu.com/")

time.sleep(2)

# 获取页面名为wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text


# 打印页面标题"百度一下，你就知道"
print(driver.title)

# 打印数据内容
print(data)

# 生成当面页面快照并保存
driver.save_screenshot("baidu.png")

# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id("kw").send_keys(u"长城")

#id = "su"是百度搜索按钮，click()是模拟点击
# driver.find_element_by_id("su").click()


#获取新的快照页面
driver.save_screenshot("长城.png")

#打印网页渲染后的源代码
print driver.page_source

#获取当前页面Cookie
print driver.get_cookie()

