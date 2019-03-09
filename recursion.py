# The base case acts as the exit condition of the recursion.


# factorial
def fact(n):
	if n == 0:  # base case
		return 1
	else:
		return n * fact(n - 1)

print(fact(1))


# number**pow
def power(num, pow):
	if pow == 0:  # base case
		return 1
	else:
		return num * power(num, pow - 1)

print(power(5, 3))


# fibonachi number
def fib(n):
	if n == 0:
		return 0  # base case
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

print(fib(8))

"""
Recursive functions can be infinite,
just like infinite while loops. These often occur
when you forget to implement the base case.
Below is an incorrect version of the factorial function.
It has no base case, so it runs until the interpreter
runs out of memory and crashes.
"""


def factorial(x):
	return x * factorial(x - 1)

# print(factorial(5))  # RecursionError: maximum recursion depth exceeded

'''
Recursion can also be indirect. One function can call a second,
which calls the first, which calls the second, and so on.
This can occur with any number of functions.
'''


def is_even(x):
	if x == 0:
		return True
	else:
		return is_odd(x-1)


def is_odd(x):
	return not is_even(x)


print(is_odd(17))  # True
print(is_even(23))  # False
