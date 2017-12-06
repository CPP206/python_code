card_infors = [{'name':'laowang', 'age':18}, {'name':'laoli', 'age':15}, {'name':'laozhao', 'age':20}]

find_name = input("请输入要查询的名字:")
for temp in card_infors:
	if temp['name'] == find_name:
		print("找到了....")
		break
else:
	print("没有找到")