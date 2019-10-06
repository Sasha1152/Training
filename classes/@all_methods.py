class MyClass:

	def func1(self):
		print('method of instance')

	@staticmethod
	def func2():
		print('staticmethod')

	@classmethod
	def func3(cls):
		print('classmethod')


a = MyClass()

a.func1()  # method of instance
a.func2()  # staticmethod
a.func3()  # classmethod

MyClass.func2()  # staticmethod
MyClass.func3()  # classmethod
