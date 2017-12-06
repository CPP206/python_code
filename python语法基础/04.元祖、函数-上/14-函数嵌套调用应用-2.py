def sum_3_nums(a, b, c):
	result = a + b + c
	print("%d + %d + %d = %d"%(a, b, c, result))
	return result

def average_3_nums(a1, a2, a3):
	result = sum_3_nums(a1, a2, a3)
	result = result / 3 #result /= 3
	print("平均值是： %d"%result)


num1 = int(input("第一个值是: "))
num2 = int(input("第二个值是: "))
num3 = int(input("第三个值是："))

average_3_nums(num1, num2, num3)