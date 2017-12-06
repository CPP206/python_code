class Cat:
	#属性

	#方法

	def eat(self):
		print("猫在吃鱼。。。。。")

	def drink(self):
		print("猫正在喝kele")

	def introduce(self):
		print("%s的年龄是:%d"%(self.name, self.age))



#创建一个对象
tom = Cat()

#调用tom指向的对象中的方法
tom.eat()
tom.drink()

#给tom指向的对象添加2个属性
tom.age = 40
tom.name = "Tom"

#获取属性的第一种方式
print("%s的年龄是： %d"%(tom.name, tom.age))


tom.introduce()

lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 10
lanmao.introduce()