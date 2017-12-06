class A:
	def __init__(self):
		self.num1 = 100
		self.__num2  =200

	def test1(self):
		print("-----test1-----")

	def __test2(self):
		print("-----test2----")

	def test3(self):
		self.__test2()
		print(self.__num2)

class B(A):
	def test5(self):
		print(self.__num2)
	def test4(self):
		self.__test2()
		print(self.__num2)

b = B()
b.test1()
b.test3()
b.test5()
b.test4()##私有属性和私有方法并不会继承