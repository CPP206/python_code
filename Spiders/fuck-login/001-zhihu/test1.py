#-*-  coding:utf-8 -*-
import requests
from requests_toolbelt import MultipartEncoder
import urllib2

headers = {
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Connection' : 'keep-alive',
	'Referer' : '',
	'Host' : '',
	'User-Agent' : ''		
}

file_payload = {
	'username' : '17626026460',
	'passwd' : '199212'
}

m = MultipartEncoder(file_payload)

print(m)
print(m.content_type)