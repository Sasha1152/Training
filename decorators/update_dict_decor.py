# https://hackernoon.com/the-goodies-of-python-decorators-66r3tsy

def dict_from_func(func):
    return {func.__name__: func}

operations = {}

@operations.update
@dict_from_func
def mul(a, b):
    return a * b

@operations.update
@dict_from_func
def add(a, b):
    return a + b

# equals this: add = operations.update(dict_from_func(add))

print(mul)  # None
print(operations)  # {'mul': <function mul at 0x7fdaf17bbae8>, 'add': <function add at 0x7fdaf16a2510>}
print(operations['mul'](2, 5))  # 10
print(operations['add'](2, 5))  # 7
