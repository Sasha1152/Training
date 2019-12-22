import functools
import sys

def trace(handle):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs,
            file=handle)
            return func(*args, **kwargs)
        return inner
    return decorator

##################

def trace(func=None, *, handle=sys.stdout):
    # со скобками
    if func is None:
        return lambda func: trace(func, handle=handle)
    # без скобок
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
    return func