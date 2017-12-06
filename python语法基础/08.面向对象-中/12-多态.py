class Dog(object):
	def print_self(self):
		print("大家好，我是XXXX")

class Xiaotq(Dog):
	def print_self(self):
		print("hello everybody,wo shi ")

def introduce(temp):
	temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)