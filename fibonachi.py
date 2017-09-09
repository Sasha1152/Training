def fib_less_then_number(n):
    result = [0]
    a, b = 0, 1
    while b < n:
        result.append(b)
        # a, b = b, a + b
        a = b
        b = a + b
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

print fib_less_then_number(60)
print fib_value_by_number(10)
