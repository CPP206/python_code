#-*- coding:utf-8 -*-
import json

strList = '[1, 2, 3, 4]'

strDict = '{"city":"北京", "name":"大猫"}'

pyList = json.loads(strList)
#[1, 2, 3, 4]
for py in pyList:
	print(py)

pyobj = json.loads(strDict)
print(pyobj['city'])
#{u'city': u'\u5317\u4eac', u'name': u'\u5927\u732b'}