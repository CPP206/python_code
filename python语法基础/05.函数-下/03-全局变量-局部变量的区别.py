#定义个全局变量，wendu

def get_wendu():
	#如果wendu这个变量已经在全局变量的位置定义了，此时还想在函数中对这个全局变量进行修改的话
	#那么，仅仅是wendu=一个值
	#这还不够，此时wendu这个变量时一个局部变量，仅仅是和全局变量的名字相同罢了
	# wendu = 33


	#使用global用来对一个全局变量的声明，那么这个函数中的wendu=33就不是定义一个局部变量，而是对全局变量进行修改
	global wendu
	wendu = 33



def print_wendu():
	print("温度是:%d"%wendu)

get_wendu()
print_wendu()