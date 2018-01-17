#-*- coding:utf-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup
import lxml
import re


url = 'https://accounts.douban.com/login'

#构造post数据
data = {
	'source':'None',
	'redir' : 'https://www.douban.com/people/148461169',
	'form_emil' : '1216938752@qq.com',
	'form_password' :'chenqi1992',
	'login' : u'登陆'
}

headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	'Host' : 'accounts.douban.com'
}

r = requests.post(url, data, headers = headers)

page = r.text
print(page)
#利用bs4获得验证码图片地址
soup = BeautifulSoup(page, 'lxml')
captcha_url = soup.find('img', id='captcha_image')
if not captcha_url is None:
	print(captcha_url)
	#利用正则获得验证码ID
	pattern = re.compile('<input type="hidden" name="captcha-id" value="(.*?)">/')
	captcha_id = re.findall(pattern, page)
	#将验证码图片保存到本地
	urllib.urlretrieve(captcha_url, 'captcha.jpg')
	captcha = raw_input("Please input the captcha: ")
	data['captcha-solution'] = captcha
	data['captcha-id'] = captcha_id

	r = requests.post(url, data = data, headers = headers)
	page = r.text
	print("成功登陆！！！！")