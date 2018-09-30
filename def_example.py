def foo(x, l=[]):
    print(x)
    l.append(x)
    print(l)
foo(1)
foo(2)

print('-' * 15)

def foo(x, l):
    print(x)
    l.append(x)
    print(l)

l = []
foo(1, l)
foo(2, l)
foo(3, l)
print(l)
