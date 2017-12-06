#用来存储名片
card_infors = []

def print_menu():
	'''完成打印功能菜单'''
	print("="*50)
	print("   名片管理系统V0.0.1")
	print(" 1.添加一个新的名片")
	print(" 2.删除一个名片")
	print(" 3.修改一个名片")
	print(" 4.查询一个名片")
	print(" 5.显示所有的名片")
	print(" 6.退出系统")
	print("="*50)


def add_new_card_infor():
	'''完成添加一个新的名片'''
	new_name = input("请输入新的名字: ")
	new_qq = input("请输入新的QQ：")
	new_weixin = input("请输入新的微信：")
	new_addr = input("请输入新的地址：")

	#定义一个新的字典，用来存储一个新的名片
	new_infor = {}
	new_infor['name'] = new_name
	new_infor['qq'] = new_qq
	new_infor['weixin'] = new_weixin
	new_infor['addr'] = new_addr
	#将一个字典添加到列表中
	global card_infors
	card_infors.append(new_infor)

def find_card_infor():
	'''用来查询一个名片'''
	global card_infors

	find_name = input("请输入你想要查找的名字：")
	for card_infor in card_infors:
		if find_name == card_infor['name']:
			print("%s\t%s\t%s\t%s"%(card_infor['name'], card_infor['qq'], card_infor['weixin'], card_infor['addr']))
			find_flage = 1
			break
	else:
		if find_flage == 0:
			print("查无此人。。。。")

def show_all_infor():
	'''显示所有的名片信息'''
	global card_infors
	print("姓名\tQQt微信t地址")
	for temp in card_infors:
		print("%s\t%s\t%s\t%s"%(temp['name'], temp['qq'], temp['weixin'], temp['addr']))

def main():
	'''完成整个程序的控制'''
	#1. 打印功能提示
	print_menu()
	while True:

		#2. 获取用户的输入
		num = int(input("请输入操作序号: "))

		#3. 根据用户的数据执行相应的功能
		if num == 1:
			add_new_card_infor()
		elif num == 2:
			pass
		elif num == 3:
			pass
		elif num == 4:
			find_card_infor()
		elif num == 5:
			show_all_infor()
		elif num == 6:
			break
		else:
			print("输入有误，请重新输入")

		print("")

#调用主函数
main()
