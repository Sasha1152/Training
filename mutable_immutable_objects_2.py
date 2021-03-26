# https://www.freecodecamp.org/news/mutable-vs-immutable-objects-python/

a = [1, 2, 3]

def do(dict1):
    dict1.append(100)

do(a)
print(a)  # [1, 2, 3, 100]

b = 1

def foo(digit):
    digit += 100
    print(digit)  # 101

foo(b)
print(b)  # 1
