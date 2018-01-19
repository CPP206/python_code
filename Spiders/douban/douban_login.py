# -*- encoding:utf-8 -*-  


'''
    1、模拟登陆豆瓣
    2、主要验证码图片获取
    3、post登陆用户和密码无加密
'''
##############################  
__author__ = "xiaopohai"
__date__ = "2018年1月17日10:07:28"


###############################  

import requests
from bs4 import BeautifulSoup
import re
import urllib

loginUrl = 'https://accounts.douban.com/login'
formData = {
    "redir": "http://movie.douban.com/mine",
    "form_email": "******",
    "form_password": "******",
    "login": u'登录',
    "source":"index_nav"
}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

r = requests.post(loginUrl, data=formData, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

a = soup.find('img', class_ = 'captcha_image')

if a is not None:
    captchaAddr = a.attrs['src']
    print(a.attrs['src'])
    pattern = re.compile(r'id=(\w*)(\W)en&size=(\w*)$')
    match = pattern.search(a.attrs['src'])
    if match:
        captchaID = match.group()[3:][:-7]

    urllib.urlretrieve(captchaAddr, 'captcha.jpg')

    #保存到本地
    captcha = raw_input('请输入验证码图片: ')
    formData['captcha-solution'] = captcha
    formData['captcha-id'] = captchaID

formData['form_email'] = '1216938752@qq.com'
formData['form_password'] = 'chenqi1992'

s = requests.session()
r = s.post(loginUrl, data = formData, headers = headers)

page = r.text
print(page)
print(r.url)
print(r.history)

