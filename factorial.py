def fact1(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def fact2(n):
    f = 1
    while n > 0:
        f = f * n
        n -= 1
    return f

def fact3(n):
    if n == 0:
        return 1
    else:
        return n * fact3(n - 1)

def fact4(n):
    f = 1
    for i in range(n):
        f *= n
        n -= 1
    return f

print fact1(5)
print fact2(5)
print fact3(5)
print fact4(5)
