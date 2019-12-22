def dec(f):
    def wrap(*args, **kwargs):
        return f'args from "{f.__name__}" function: {args, kwargs}, result: {f(*args, **kwargs)}'
    return wrap

@dec
def func(a, b):
    return a + b

print(func(1, 2))  # args from "func" function: ((1, 2), {}), result: 3

@ dec
def func2(a, b, c):
    return a + b + c

print(func2('a', 'b', c='100'))  # args from "func2" function: (('a', 'b'), {'c': '100'}), result: ab100