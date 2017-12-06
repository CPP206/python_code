def etst(a, b):
	def test_in(x):
		print(a*x+b)
	return test_in

line1 = test(1, 1)
line1(0)
line2 = test(10, 4)
line2(0)