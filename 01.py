a = [4, 2, 3, 0, 1, 12, -4, -44]


imax = 0
for i in range(len(a)):
    n = i
    while n < len(a):
        if a[i] < a[n]:
            imax = i
        n += 1
    a[i] = a[imax]
print a