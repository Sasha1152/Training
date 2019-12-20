def foo(x, l=[]):
    l.append(x)
    print(x, l)

foo(1)  # 1 [1]
foo(2)  # 2 [1, 2]
foo(3)  # 3 [1, 2, 3]
print('------'*3)


def foo(x, l):
    l.append(x)
    print(x, l)

l = []
foo(1, l)  # 1 [1]
foo(2, l)  # 2 [1, 2]
foo(3, l)  # 3 [1, 2, 3]
print('------'*3)


def f(a = 0):
    a += 1  # Операція присвоєння по замовчуванню створює змінну у локальній області видимості
    print(a)

f()  # 1
f()  # 1
f()  # 1
print('------'*3)


def unique(iterable, seen=set()):
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc

print(unique.__defaults__)  # (set(),)
l = [1, 1, 2, 3]
print(unique(l))  # [1, 2, 3]
print(unique.__defaults__)  # ({1, 2, 3},)
print(unique(l))  # []
print(unique.__defaults__)  # ({1, 2, 3},)
print('------'*3)


def unique_better(iterable, seen=None):
    seen = set(seen or [])  # equivalent: seen = set()
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc

print(unique_better.__defaults__)  # (None,)
l = [1, 1, 2, 3]
print(unique_better(l))  # [1, 2, 3]
print(unique_better.__defaults__)  # (None,)
print(unique_better(l))  # [1, 2, 3]
print(unique_better.__defaults__)  # (None,)
