def foo(first, second):
	print('First: %s, second: %s' %(first, second))

# foo_1 = lambda x: lambda y: foo(first, second)

def foo_2(first):
	def new_foo(second):
		return foo(first, second)
	return new_foo