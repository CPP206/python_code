#-*- coding:utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
from lxml import etree

def captcha(data):
	with open('captcha.jpg', 'wb') as fp:
		fp.write(data)
	time.sleep(1)
	return raw_input("请输入验证码： ")

def zhihuLogin():
	#构建一个保存Cookie的值的session对象
	sessiona = requests.Session()
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
	#获取页面信息，找到需要POST的数据(并且记录到当前页面的Cookie)
	html = sessiona.get('https://www.zhihu.com/#signin', headers=headers).content
	# e = etree.HTML(html)
	# print(html)
	# _xsrf = e.xpath('//input[@name="_xsrf"]/@value')
	#找到name属性为_xsrf的input属性，取出value里的值。74c58fc1cc34fcad58dc3490473a127f
	_xsrf = BeautifulSoup(html, "lxml").find('input', attrs={'name', '_xsrf'}).get('value')
	print(type(_xsrf))

	#取出验证码，r后面的值是Unix时间戳，time.time()
	captchar_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)

	response = sessiona.get(captchar_url, headers = headers)

	data = {
		"_xsrf" : _xsrf,
		"email" : "1216938752@qq.com",
		"password": "199212",
		"remember_me" : True,
		"captcha" : captcha(response.content)
	}

	response = sessiona.post('https://www.zhihu.com/login/email', data=data, headers=headers)

	print(response.text.encode('UTF-8'))

	# response = sessiona.get('https://www.zhihu.com/people/chen-qi-26-76/answers', headers = headers)

	print(response.text.encode('utf-8'))

if __name__ == "__main__":
	zhihuLogin()