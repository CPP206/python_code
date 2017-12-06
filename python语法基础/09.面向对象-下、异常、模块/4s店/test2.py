class CarStore(object):
	def order(self, car_type):
		if car_type == "索纳塔":
			return Suonata()
		if car_type == "名图":
			return Mingtu()

class Car(object):
	def move(self):
		print("车在移动。。。。")
	def musice(self):
		print("正在播放音乐。。。。")
	def stop(self):
		print("车在停止。。。")

class Suonata(Car):
	def __init__(self):
		self.__name = "索纳塔"
		super(Suonata, self).__init__()

class Mingtu(Car):
	def __init__(self):
		self.__name = "名图"
		super(Mingtu, self).__init__()

car_store = CarStore()
car = car_store.order("索纳塔")
car.move()
car.music()
car.stop()