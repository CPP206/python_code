class Cat:
	#属性

	#方法
	def eat(self):
		print("猫在吃鱼。。。。。")

	def drink(self):
		print("猫正在喝可乐")


	def introduce(self):
		print("%s的年龄是：%d"%(tom.name, tom.age))


#创建一个对象
tom = Cat()

#调用tom指向的对象中的方法
tom.eat()
tom.drink()

#给tom指向的对象添加两个属性
tom.name = "Tom"

tom.age = 12

#获取属性的第一种方法
print("%s的年龄是:%d"%(tom.name, tom.age))


tom.introduce()