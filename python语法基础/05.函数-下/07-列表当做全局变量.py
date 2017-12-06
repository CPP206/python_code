nums = [11, 22, 33]
infor = {'name':'laowang'}

def test():
	nums.append(44)
	infor['age'] = 17

def test2():
	print(nums)
	print(infor)

test()
test2()