def log(text):
	def dectorator(func):
		def wrapper(*args, **kw):
			print("%s %s(): "%(text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return dectorator#

#@log("excuate")#
def now():
	print("2017年10月26日20:13:23")

now = log("excuate")(now)

now()