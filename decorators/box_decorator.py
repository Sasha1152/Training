def decorator(f):
	def wrapper(a, b, c):
		print('Begin')
		print('a=' + str(a), 'b=' + str(b), 'c=' + str(c))
		print('V =', f(a, b, c))
		print('End')
		print('---' * 6)
	return wrapper


@decorator  # or box = decorator(box)
def box(a, b, c):
	return a * b * c

box(2, 3, 4)
box(10, 10, 20)
