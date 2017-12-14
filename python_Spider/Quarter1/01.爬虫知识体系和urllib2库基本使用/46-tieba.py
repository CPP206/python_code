#-*- coding:utf-8 -*-

import urllib
import urllib2
import random

def choiceList():
	#可以是User-Agent列表，也可以是代理列表
	ua_list = [
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
	        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
	        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
	        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
	        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
	]
	return random.choice(ua_list)

def loadPage(url, filename):
	"""
		作用：根据url发送请求，获取服务器相应文件
		url：需要爬取的url地址
		filename：处理的文件名
	"""
	print("正在下载："+filename)
	request = urllib2.Request(url)
	request.add_header("User-Agent", choiceList())
	return urllib2.urlopen(request).read()

def writePage(html, filename):
	"""
		作用：将html内容写入到本地
		html：服务器相应文件内容
		filename：文件名
	"""
	print("正在保存："+filename)
	#文件写入
	with open(filename.decode("UTF-8"), "w") as f:
		f.write(html)
		print("-"*30)

def tiebaSpider(url, beginPage, endPage):
	"""
		作用：贴吧爬虫调度器，负责组合处理每个页面

		url：贴吧url的前部分
		beginPage：起始页
		endPage：结束页
	"""
	for page in range(beginPage, endPage+1):
		pn = (page -1) * 50
		filename = "第" +str(page) + "页.html"
		fullurl = url + "&pn=" +str(pn)
		html = loadPage(fullurl, filename)
		writePage(html, filename)
		print("谢谢使用！！！")

if __name__ == "__main__":
	kw = raw_input("请输入需要爬取的贴吧名字：")
	beginPage = int(raw_input("请输入起始页："))
	endPage = int(raw_input("请输入结束页："))

	url = "http://tieba.baidu.com/f?"
	key = urllib.urlencode({"kw":kw})
	fullurl = url+key
	tiebaSpider(fullurl, beginPage, endPage)