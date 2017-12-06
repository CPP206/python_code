def test(a, b, func):
	result = func(a, b)
	return result

func_new = input("请输入一个匿名函数:")
func_new = eval(func_new)

num = test(11, 22, func_new)

print("num的值是: %d"%num)