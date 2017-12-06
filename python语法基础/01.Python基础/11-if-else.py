age = input("请输入你的年龄： ")
#input获取所有的数据，都当做字符串类型20 --->age --->"20"

age_num = int(age)

if age_num > 18:
	print("已成年，可以直接去网吧嗨皮...")
else:
	print("未成年，回家写作业吧。。。")