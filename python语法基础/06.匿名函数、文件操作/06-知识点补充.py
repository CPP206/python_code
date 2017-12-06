'''
+=表达式：
	1、参数指向了可变的，就在原来的基础上更改
	2、参数指向了不可变的，就相当于num = num + num,修改了参数的指向

num = num + num
	不管指向哪一种参数，都不改变原始参数
	
'''


# a = 100
a = [100]

def test(num):
	# num += num # +=表示num指向谁就对谁进行修改，如果num指向[100]， 那么就变成[100, 100]
	#如过num指向100，因为100是不可变类型，所以不能修改，所以num = num + num

	num = num + num

	 # 注意只要是num = xxx一定是num指向了一个新的地址

	print(num)


test(a)

print(a)