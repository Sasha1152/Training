def f():
	try:
		f.a += 1
	except AttributeError:
		f.a = 1
	return f'function was run {f.a} times'

f()
print(f())
f()
print(f.a)  # 3
