def foo(x, y, z, a):
	print(x + y)

nums = [1, 2, 3, 4]
print(nums.index(2))
foo(*nums)

foo(*(1, 2, 3, 4))
foo(*[1, 2, 3, 4])
foo(*{1, 2, 3, 4})