def decorator(f):
	def wrapper(a, b, c):
		print('Begin')
		print('a=' + str(a), 'b=' + str(b), 'c=' + str(c))
		print('V =', f(a, b, c))
		print('End')
	return wrapper


@decorator  # or box = decorator(box)
def box(a, b, c):
	return a * b * c

box(2, 3, 4)
print('---' * 6)
box(10, 10, 20)
