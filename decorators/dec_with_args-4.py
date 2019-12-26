# https://hackernoon.com/the-goodies-of-python-decorators-66r3tsy

def print_decorator(func):
    def wrapper(*args, **kwargs):
        print('function', func.__name__, 'called with args - ', args, 'and kwargs - ', kwargs)
        result = func(*args, **kwargs)
        print('function', func.__name__, 'returns', result)
        return result
    return wrapper


@print_decoratore
def mul(a, b):
    return a * b

print(mul(2, 3))


@type
def func1():
    return 1

print(func1)  # <class 'function'>

@print
def func2():
    return 1

print(func2)  # <function func2 at 0x7f6f75e265e0> , None
