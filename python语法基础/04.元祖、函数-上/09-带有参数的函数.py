#定义了一个函数
def sum_2_nums(a, b):
	result = a + b
	print("%d + %d = %d"%(a, b, a+b))


num1 = int(input("请输入第1个数字: "))
num2 = int(input("请输入第2个数字："))

#调用函数
sum_2_nums(num1, num2)