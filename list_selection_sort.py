a = [3, 2, -1, 1, 0]

for j in range(len(a)):
    i_min = j
    print i_min
    for i in range(j, len(a)):
        if a[i] <= a[i_min]:
            i_min = i
    print a[i_min]
    print a
    a[j], a[i_min] = a[i_min], a[j]
    print a

print '---' * 5

a = [3, 2, 1, 4]
for j in range(len(a) - 1):
        i_min = j
        i = j + 1
        while i < len(a):
            if a[i] < a[i_min]:
                i_min = i
            i += 1
        a[j], a[i_min] = a[i_min], a[j]
print a
