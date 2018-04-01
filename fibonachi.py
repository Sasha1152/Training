def fib_less_then_number(n):
    result = [0]
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def fib_value_by_number(n):
    a, b = 0, 1
    if n == 0:
        return a
    else:
        while n != 1:
            b = a + b
            a = b - a
            n -= 1
        return b


def fib2(n):
    a = 0
    b = 1
    while b < n:
        print(a)
        print(b)
        a=a+b
        b=a+b


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib3(x):
    a = 0
    b = 1
    for i in range(2, x):
        b, a = (a + b), b
    return b


print(fib_less_then_number(60))
print('-'*8)
print(fib_value_by_number(10))
print('-'*8)
print(fib(10))
print('-'*8)
print(fib2(60))
print('-'*8)
print(fib3(8))

