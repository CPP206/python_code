class Store(object):
	def select_car(self):
		pass

	def order(self, car_type):
		return self.select_car(car_type)


class BMWCarStore(Store):
	def select_car(self, car_ype):
		return BMWFactory().select_car_by_type(car_ype)


class BMWFactory(object):
	def select_car_by_type(self, car_type):
		if car_type == "mini":
			return Suonata()
		elif car_type == "720li":
			return Mingtu()
		elif car_type == "x6":
			return Ix35()

class CarStore(Store):
	def select_car(self, car_type):
		return Factore().select_car_by_type(car_type)

