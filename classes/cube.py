class Cube:
	def __init__(self, a, b=None, c=None):
		self.a = a
		self.b = b
		self.c = c

	def get_volume(self):
		if not (self.b and self.c):
			return self.a ** 3
		elif not self.c:
			return self.a ** 2 * self.b
		return self.a * self.b * self.c

cube = Cube(3, 3, 3)
print(cube.get_volume())
