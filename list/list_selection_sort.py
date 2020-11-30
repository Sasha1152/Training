a = [3, 2, -1, 1, 0]

for j in range(len(a)):
    i_min = j
    print(i_min)
    for i in range(j, len(a)):
        if a[i] <= a[i_min]:
            i_min = i
    print(a[i_min])
    print(a)
    a[j], a[i_min] = a[i_min], a[j]
    print(a)
print('---' * 5)

a = [3, 2, 1, 4]
for j in range(len(a) - 1):
        i_min = j
        i = j + 1
        while i < len(a):
            if a[i] < a[i_min]:
                i_min = i
            i += 1
        a[j], a[i_min] = a[i_min], a[j]
print(a)


a = [4, 2, 3, 0, 1, 12, -4, -44]
for i in range(len(a)):
    imin = i
    for j in range(i, len(a)):
        if a[j] < a[imin]:
            imin = j
    a[i], a[imin] = a[imin], a[i]
print(a)