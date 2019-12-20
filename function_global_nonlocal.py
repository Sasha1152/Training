var = 1

def foo():
    var = 2
    return var

print(var)  # 1
print(foo())  # 2
print(var)  # 1
print('----'*2)


def foo2():
    global var
    var = 2
    return var

print(foo2())  # 2
print(var)  # 2
print('----'*2)


def counter():
    a = 0
    def incrementer():
        nonlocal a
        a += 1
        return a
    return incrementer

print(counter())  # <function foo3.<locals>.incrementer at 0x005EFA08>
f = counter()
print(f())  # 1
print(f())  # 2
print(f())  # 3