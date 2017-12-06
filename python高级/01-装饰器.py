def log(func):
	def wrapper(*args, **kw):
		print("call %s(): "%func.__name__)  #使用了闭包
		return func()
	return wrapper

@log
def now():
	print("2017年10月26日19:42:41")



now()