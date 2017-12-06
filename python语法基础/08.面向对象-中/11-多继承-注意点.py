class Base(object):
	def test(self):
		print("-----Base")

class A(Base):
	def test(self):
		print("------A")


class B(A):
	def cc():
		print("cccc")
	def test(self):
		print("-----B")

class C(A,B):
	pass

c = C()
c.test()
print(C.__mro__)