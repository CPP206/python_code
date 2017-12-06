class Dog:
	def __del__(self):
		print("英雄over------------")

dog1 = Dog()
dog2 = dog1   #这里是引用赋值，如果是重新创建了一个对象，那么就del调用两次了

del dog1
print("======================")
del dog2



#如果程序结束时，有些对象还存在，那么python解释器就会自动调用它们的__del__方法来清理工作