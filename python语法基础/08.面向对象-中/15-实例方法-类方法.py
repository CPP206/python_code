'''
方法访问属性
1、普通方法可以访问类属性，使用self.类属性或者类.类属性
2、类方法访问类属性，使用cls.类属性或者类.类属性

3、类方法无法访问实例属性

4、静态方法只能通过传值的方式或者类.类属性的方式访问类属性
'''


class Game():
	#类属性
	num = 10

	def __init__(self, new_name):
		self.name = new_name

	def test1(self):
		print(Game.num)
		print(self.num)

	@classmethod
	def class_test(cls):
		print(cls.num)
		print(Game.num)

	@staticmethod
	def static_test():
		print(Game.num)

game = Game("test")
print("普通方法访问类属性------")
print(game.num)
game.test1()
print("类属性访问类方法------")
Game.class_test()
game.class_test()  ##这里可以通过类名或者这个类创建的对象去调用这个类方法


print("静态方法放问类属性----")
game.static_test()