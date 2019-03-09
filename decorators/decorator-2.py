def decor(func):
	def wrap():
		print("============")
		func()
		print("============")
	return wrap


def decor_2(func):
	def wrap():
		print("============")
		func()
		print("============")
	return wrap()


def print_text():
	print("Hello world!")

decorated = decor(print_text)
decorated()

decor_2(print_text)

print_text = decor(print_text)  # or just write @decor before print_text
print_text()  # function will be decorated
