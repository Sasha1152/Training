a = [3, 2, 1, 4]

i_min = 0
for j in range(1, len(a)):
    for i in range(j, len(a)):
        if a[i_min] >= a[i]:
            i_min = i
        print a[i]
    a[i], a[i_min] = a[i_min], a[i]

print a
print '---' * 5

a = [3, 2, 1, 4]
for k in range(len(a) - 1):
        m = k
        i = k + 1
        while i < len(a):
            if a[i] < a[m]:
                m = i
            i += 1
        t = a[k]
        a[k] = a[m]
        a[m] = t
print a