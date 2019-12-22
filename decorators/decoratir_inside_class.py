# https://habr.com/ru/post/141501/

def decorator(method_to_decorate):
	print('OK')
	def wrapper(self, n):
		n = n - 3
		return method_to_decorate(self, n)
	return wrapper


class Lucy(object):
	def __init__(self, age):
		self.age = age

	@decorator  # 'OK' will printed
	def get_age(self, n):
		print("I am %s years old!" % (self.age + n))


l = Lucy(100)
l.get_age(-3)
