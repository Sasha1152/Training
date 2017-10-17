a = [4, 2, 3, 0, 1, 12, -4, -44]

for i in range(len(a)):
    imin = i
    for j in range(i, len(a)):
        if a[j] < a[imin]:
            imin = j
    a[i], a[imin] = a[imin], a[i]
print a