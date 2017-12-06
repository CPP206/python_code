class Dog:

	def __init__(self, new_name):
		self.__name = new_name
		self.__age = 0
		#定义了一个私有的属性，属性
	def set_age(self, new_age):
		if new_age > 0 and new_age <= 100:
			self.__age = new_age
		else:
			self.__age = 0

	def get_age(self):
		return self.__age



dog = Dog("小白")

dog._Dog__age = 10    #python内部已经把私有属性的名称给改了
age = dog.get_age()
print(age)

dog.set_age(3)
age = dog.get_age()
print(age)