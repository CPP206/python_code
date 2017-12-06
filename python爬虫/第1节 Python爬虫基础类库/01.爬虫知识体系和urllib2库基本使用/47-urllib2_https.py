#-*- coding:utf-8 -*-

import urllib2
import ssl

def choiceHeader():
	ua_agent = [
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
	]
	return random.choice(ua-agent)


if __name__ == "__main":
	#忽略SSL安全认证
	context = ssl._create_unverified_context()
	#url = "https://www.12306.cn/normhweb/"
	url = "https://www.baidu.com/"
	request = urllib2.Request(url)
	request.add_header("User-Agent", choiceHeader())

	response = urllib2.urlopen(request, context= context)
	print(response.read())