def test(a, b, func):
	result = func(a, b)
	return result

num = test(11, 12, lambda x, y : x+y)

print("test的取值是: %d"%num)