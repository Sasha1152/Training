class A:
	def spam(self):
		print(1)


class B(A):
	def spam(self):
		print(2)
		super().spam()  # calls the spam method of the superclass

	def mess(self):
		super().spam()

B().spam()  # 2 1
B().mess()  # 1
