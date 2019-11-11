def foo(first, second):
	print('First: %s, second: %s' % (first, second))

# foo1 = lambda x: lambda y: foo(first, second)


def foo2(first):
	def new_foo(second):
		return foo(first, second)
	return new_foo

foo('a', 'b')

print(foo2('a'))