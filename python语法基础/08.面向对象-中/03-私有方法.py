class Dog:
	#私有方法
	def __send_msg(self):
		print("--------正在发送短信------")

	#公有方法
	def send_msg(self, new_money):
		if new_money>100000:
			self.__send_msg()
		else:
			print("余额不足，请先充值")


dog = Dog()
dog.send_msg(1000000)
dog._Dog__send_msg()  #私有方法也是同样，在python内部名称被改掉