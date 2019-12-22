# https://www.youtube.com/watch?v=h_B3O5jWMi4&list=PLlb7e2G7aSpTTNp7HBYzCBByaE1h54ruW&index=3
import functools

def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner


@trace
def identity(x):
    """I do nothing useful."""
    return x

print(identity(42))
# help(identity)
print(identity.__name__, identity.__doc__, identity.__module__)  # inner None __main__
print("----"*3)

#################

# def trace(func):
#     def inner(*args, **kwargs):
#         print(func.__name__, args, kwargs)
#         return func(*args, **kwargs)
#
#     inner.__module__ = func.__module__
#     inner.__name__ = func.__name__
#     inner.__doc__ = func.__doc__
#     return inner

# OR:
# def trace(func):
#     def inner(*args, **kwargs):
#         print(func.__name__, args, kwargs)
#         return func(*args, **kwargs)
#     functools.update_wrapper(inner, func)
#     return inner

# OR:    
def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner



@trace
def identity(x):
    """I do nothing useful."""
    return x

print(identity(42))
# help(identity)
print(identity.__name__, identity.__doc__, identity.__module__)  # identity I do nothing useful. __main__
print('----'*3)

####################
# With toggle of decorator

trace_enabled = False

def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner if trace_enabled else func