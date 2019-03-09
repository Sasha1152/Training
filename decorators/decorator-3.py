def talk(n=1):

	def good():
		return 'GOOD!'

	def bad():
		return 'BAD!'

	if n == 1:
		return good
	else:
		return bad


print(talk)  # <function talk at 0x007E7858>
print(talk())  # <function talk.<locals>.good at 0x00527810>
print(talk(2))  # <function talk.<locals>.bad at 0x00527738>
print(talk()())  # GOOD!
# or the same:
t = talk()
print(t())  # GOOD!
print(talk(2)())  # BAD!


def decorator(func):
	print('Begin')
	print(func())
	print('The end')

decorator(t)
