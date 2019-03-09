def generator():
	for i in [1, 2, 3]:
		yield i

g = generator()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g, 'the end'))

# for i in range(5):
# 	print(next(g, 'the end'))
