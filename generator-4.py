def generator(n):
	for i in range(n):
		yield i

g = generator(5)
print(g)  # <generator object generator at 0x006818A0>
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
print(next(g, 'the end'))  # 3

print('--' * 5)

g2 = generator(2)
print(next(g2))  # 0
print(next(g2))  # 1
print(next(g2, 'the end'))  # the end

print('--' * 5)

generator3 = (x ** 2 for x in range(3))
print(generator3)  # <generator object <genexpr> at 0x00681A20>
print(next(generator3))  # 0
print(next(generator3))  # 1

print('--' * 5)

generator4 = (x ** 2 for x in range(3))
print('list: ', list(generator4))  # [0, 1, 4]
print('list: ', list(generator4))  # []
for i in generator4:
	print(i)  # nothing

print(range(20) == range(0, 20))  # True
