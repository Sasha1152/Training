import functools


def memoized(func):
    cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        print(cache)
        return cache[key]
    return inner


@ memoized
def func(a, b):
    return a + b

print(func(1, 2))
