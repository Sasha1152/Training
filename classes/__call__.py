"""
Метод __call__() автоматически вызывается,
когда к объекту обращаются как к функции
"""

class Changeable:
    def __init__(self, color):
        self.color = color

    def __call__(self, newcolor):
        self.color = newcolor

    def __str__(self):
        return "%s" % self.color


canvas = Changeable("green")
frame = Changeable("blue")
print(canvas, frame)  # green blue

canvas("red")
frame("yellow")
print(canvas, frame)  # red yellow

print('---'*3)
#########################################

import functools
import sys

class Trace:
    def __init__(self, handle):
        self.handle = handle

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs,
            file=self.handle)
            return func(*args, **kwargs)
        return inner

@Trace(sys.stderr)
def identity(x):
    return x

print(identity(1))  # 1  identity (1,) {}
