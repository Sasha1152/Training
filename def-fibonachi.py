def fib(n):
    print("Функция с return")
    result = []
    a, b = 0, 1
    while b < n:
        result.append(a)
        result.append(b)
        a= a + b
        b=a+b
    return result
print(fib(100))
