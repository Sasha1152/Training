# factorial
def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n - 1)

print(fact(5))

# number**pow
def power(num, pow):
	if pow == 0:
		return 1
	else:
		return num * power(num, pow - 1)

print(power(5, 3))

# fibonachi number
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

print(fib(8))