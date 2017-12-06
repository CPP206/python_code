class Cat:
	'''定义了一个Cat类'''
	#初始化对象
	def __init__(self, new_name, new_age):
		self.name = new_name
		self.age = new_age

	#方法
	def eat(self):
		print("猫正在吃鱼")

	def drink(self):
		print("猫在喝可乐")

	def introduce(self):
		print("%s的年龄是: %d"%(self.name, self.age))

#创建一个对象
tom = Cat("Tom",40)

tom.eat()
tom.drink()
tom.introduce()


lanmao = Cat("蓝猫", 10)
lanmao.introduce()