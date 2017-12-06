def test():
	a = 11
	b = 22
	c = 33

	#第一种，用一个列表来封装3个变量的值
	return a, b, c


num = test()
print(num)

a, b, c = test()
print("a=%d, b=%d, c=%d"%(a, b, c))