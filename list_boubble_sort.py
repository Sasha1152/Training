a = [3, 1, 2, 0]

n = 1
while n < len(a):
    for i in range(len(a) - n):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] =\
                a[i + 1], a[i]
    n += 1
print(a)
print('---'*5)

a = [3, 1, 2]

n = len(a)
while n:
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] =\
                a[i + 1], a[i]
    n -= 1
print(a)
print('---'*5)

a = [3, 0.5, 2, 1]

changed = True
while changed:
    changed = False
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] =\
                a[i + 1], a[i]
            changed = True
print(a)
print('---'*5)

a = [3, 2, 1, 0]

n = len(a)
while n:
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            a[i - 1], a[i] = a[i], a[i - 1]
        # print a
    n -= 1
    # print a
print(a)
