def foo(*args):
	print(args[2])

foo(0, 1, 2, 3, 4)


a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5, 6, 7, 8]
print(d)  # 9


def func(**kwargs):
	print(kwargs['c'])

func(a='one', b='two', c='three')  # three
