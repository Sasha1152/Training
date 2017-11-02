class Coyote():
	@staticmethod
	def voice():
		print('Uuuuu..uuuuu..uuu')

	@classmethod
	def voice_2(cls):
		print('Rrrr..rr')

Coyote.voice()  # Uuuuu..uuuuu..uuu
Coyote.voice_2()  # Rrrr..rr

class MyClass:

	@staticmethod
	def func1(x, y):
		return x + y

	def func2(self, x, y):
		return x + y

	def func3(self, x, y):
		return MyClass.func1(x, y)

print(MyClass.func1(10, 20))  # 30
c = MyClass()
print(c.func1(1, 2))  # 2
print(c.func2(2, 3))  # 5
print(c.func3(3, 4))  # 7