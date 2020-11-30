a = [3, 2, 1, 0]

for i in range(1, len(a)):
    j = i - 1
    key = a[i]
    while (a[j] > key) and (j >= 0):
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key

print(a)

print('---' * 5)

a = [3, 2, 1, 0]
for i in range(1, len(a)):
    key = a[i]
    n = 1
    while key < a[i - n] and (i - n) >= 0:
        a[i - n + 1] = a[i - n]
        n += 1
    a[i - n + 1] = key
print(a)

print('---' * 5)

a = ['c', 'b', 'a']
for i in range(1, len(a)):
    key = a[i]
    n = i
    while n > 0 and key < a[n - 1]:
        a[n] = a[n - 1]
        n -= 1
    a[n] = key
print(a)

a = ['c', 'b', 'a', 2, 8, -9]
for i in range(1, len(a)):
    temp = a[i]
    while i:
        if a[i - 1] > temp:
            a[i], a[i - 1] = a[i - 1], temp
        i -= 1
print(a)

a = [8, 6, 7, 2, 3, 4, 1]
for i in range(1, len(a)):
    key = a[i]
    print('key = ', key)
    j = 1
    while i >= j:
        if key < a[i - j]:
            a[i - j + 1], a[i - j] = a[i - j], key
        j += 1
        print(a)