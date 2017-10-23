class Person:
	def help(self):
		print('heeeeep')

class Duck:
	def help(self):
		print('Quaaaaak')

class SomethingElse:
	pass

def InTheForest(x):
	x.help()

donald = Duck()
john = Person()
who = SomethingElse()

for thing in [donald, john, who]:
	try:
		InTheForest(thing)
	except AttributeError:
		print('Meeooww')