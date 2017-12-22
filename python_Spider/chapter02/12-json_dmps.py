#-*- coding:utf-8 -*-

import json
import chardet

listStr = [1, 2, 3, 4]
tupleStr = (1, 2, 3, 4)
dictStr  = {"city":"北京", "name":"大猫"}

print(type(json.dumps(listStr)))
# '[1, 2, 3, 4]'

print(type(json.dumps(tupleStr)))
# '[1, 2, 3, 4]'

#注意，json.dumps()序列化时默认使用ascii编码
#添加参数 ensure_ascii = False,禁用ascii编码，按utf-8编码
#chardet.detect()返回字典，其中confidence是检测精确度。

print(json.dumps(dictStr))
#'{"city":"\\u5317\\u4eac", "name":"\\u5927\\u5218"}'

print(chardet.detect(json.dumps(dictStr)))

print(json.dumps(dictStr, ensure_ascii=False))

print(chardet.detect(json.dumps(dictStr, ensure_ascii=False)))

