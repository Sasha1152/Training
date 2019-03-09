class A:
	def method(self):
		print("A method")


class B(A):
	def another_method(self):
		print("B method")


class C(B):
	def third_method(self):
		print("C method")


c = C()
c.method()  # A method
c.another_method()  # B method
c.third_method()  # C method
