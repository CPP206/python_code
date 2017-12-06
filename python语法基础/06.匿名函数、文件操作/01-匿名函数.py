def test1(a, b):
	return a+b

result1 = test1(11, 22)

test2 = lambda a, b: a + b

result2 = test2(11, 22)
result3 = test2(11, 22)

print("result1=%d, result2 = %d"%(result1, result2))

print("再重新调用一次匿名函数: result2：%d"%result3)