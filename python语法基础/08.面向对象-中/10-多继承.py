class Base(object):
	def test(self):
		print("-----Base-----")

class A(Base):
	def test1(self):
		print("-----test1")
	def test(self):
		print("------AAAAA----")

class B(Base):
	def test2(self):
		print("-----test2")
	def test(self):
		print("----BBBBB---")

class C(A,B):
	pass

c = C()
c.test()
c.test1()
c.test2()