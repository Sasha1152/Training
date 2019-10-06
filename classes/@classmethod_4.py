class MyClass:
	@classmethod
	def method(cls):
		print(cls.__name__)


class MySubclass(MyClass):
	pass

MyClass.method()  # MyClass
MySubclass.method()  # MySubclass
