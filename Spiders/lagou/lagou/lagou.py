#-*- coding:utf-8 -*-
import os
import requests
import urllib
import urllib2
import hashlib
# from lxml import etree
from bs4 import BeautifulSoup

#使用sesseion请求对象
session = requests.session()

HEADERS = {
	'Referer' : 'https://passport.lagou.com/login/login.html',
	'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0',
	'X-Requested-With' : 'XMLHttpRequest',
	'Cookie' : '_ga=GA1.2.430365608.1515732992; _gid=GA1.2.1882109019.1515732992; JSESSIONID=ABAAABAAAGHAABH5EC8B671815C3C1531C243D2F549801A; user_trace_token=20180112125634-f69c848d-f754-11e7-a29d-5254005c3644; LGUID=20180112125634-f69c8d9d-f754-11e7-a29d-5254005c3644; X_HTTP_TOKEN=5ac37b80362fe868a86056effa6d87f7; _ga=GA1.3.430365608.1515732992; TG-TRACK-CODE=undefined; index_location_city=%E4%B8%8A%E6%B5%B7; ab_test_random_num=0; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515732993,1515748461; LGSID=20180113092210-2d36aa3a-f800-11e7-a2e1-5254005c3644; gate_login_token=9884489973efb45ee9648e3e5fb1581d20b26f219ef3bbe0; login=false; unick=""; _putrc=""; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515809282; LGRID=20180113100804-96c37ccd-f806-11e7-93e3-525400f775ce'
}


#针对密码进行双重加密
def encrypyPwd(passwd):
	g = 'veenike'
	#对密码进行了md5双重加密
	passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()

	#weennike这个是是在js文件中找到的一个写死的值
	passed = g + passwd + g

	passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()

	return passwd

#获取请求token
def getTokenCode():
	login_page = 'https://passport.lagou.com/login/login.html';

	data = session.get(login_page, headers = HEADERS)
	soup = BeautifulSoup(data.content, "lxml")
	'''
		页面新添加了下面这个东西，所以要从登陆页面提取token,code,在头信息里面添加
		<script type="text/javascript">
            window.X_Anti_Forge_Token = 'dde4db4a-888e-47ca-8277-0c6da6a8fc19';
            window.X_Anti_Forge_Code = '61142241';
        </script>
	'''
	anti_token = {'X-Anti-Forge-Token' : 'None', 'X-Anti-Forge-Code' : '0'}

	# x = soup.find_all('script')[1].string.strip(" \n").splitlines()
	#map函数的意思是传递一个函数和一个序列，针对序列的每一个元素都操作一个函数
	anti_token['X-Anti-Forge-Token'], anti_token['X-Anti-Forge-Code'] = map(
		lambda x:
			x.split('=')[1].strip(' ;\'')    #这里的删除序列是只要只要边（开头或结尾）上的字符在删除序列内，就删除掉。
		,
		soup.find_all('script')[1].string.strip(' \n').splitlines()
	)
	return anti_token



#登陆操作
def login(user, passwd, captchaData = None, token_code = None):
	postData = {
		'isValidate' : 'true',
		'password' : passwd,
		#如需验证码，则添加验证码
		'request_form_verifycode' : (captchaData if captchaData != None else ''),
		'submit' : '',
		'username' : user
	}

	login_url = "https://www.lagou.com/login/login.json"
	#头信息添加tokena
	login_headers = HEADERS.copy()
	login_headers['Referer'] = 'https://passport.lagou.com/login/login.html?'
	login_headers['Host'] = 'passport.lagou.com'
	login_headers['Origin'] = 'https://passport.lagou.com'
	login_headers['Cookie'] = '_ga=GA1.2.430365608.1515732992; _gid=GA1.2.1882109019.1515732992; JSESSIONID=ABAAABAAAGHAABH5EC8B671815C3C1531C243D2F549801A; user_trace_token=20180112125634-f69c848d-f754-11e7-a29d-5254005c3644; LGUID=20180112125634-f69c8d9d-f754-11e7-a29d-5254005c3644; X_HTTP_TOKEN=5ac37b80362fe868a86056effa6d87f7; _ga=GA1.3.430365608.1515732992; TG-TRACK-CODE=undefined; index_location_city=%E4%B8%8A%E6%B5%B7; ab_test_random_num=0; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515732993,1515748461; LGSID=20180113092210-2d36aa3a-f800-11e7-a2e1-5254005c3644; gate_login_token=9884489973efb45ee9648e3e5fb1581d20b26f219ef3bbe0; login=false; unick=""; _putrc=""; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515809582; LGRID=20180113100805-96c37ccd-f806-11e7-93e3-525400f775ce'

	token_code = getTokenCode() if token_code is None else token_code
	login_headers.update(token_code)

	print(login_headers['X-Anti-Forge-Code'])

	# data = {'content' : {"rows" : []}, "message" :"该账号不存在或密码错误，请重新输入", "state" : 400}
	response = session.post(login_url, data = postData, headers = login_headers)
	print(login_headers['Cookie'])
	print(response.content)

if __name__ == "__main__":
	# username = str(raw_input("请输入你的手机号或者邮箱\n >>>:"))
	# passwd = str(raw_input("请输入你的密码\n >>>:"))
	username = "17626026460"
	passwd = "chenqi1992"
	passwd = encrypyPwd(passwd)

	data = login(username, passwd)