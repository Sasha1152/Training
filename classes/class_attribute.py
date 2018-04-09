class A():
	arg = 'tree'

	def f(self):
		return self.arg

ins1 = A()
ins2 = A()

print(ins1.f())
print(ins2.f())
ins1.arg = 'bush'
print(ins1.f())
print(ins2.f())