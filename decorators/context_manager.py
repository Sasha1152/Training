from contextlib import contextmanager


@contextmanager
def test():
	print('Before')
	yield
	print('After')

with test():
	print('Testing context manager')

