a = [3, 2, 1, 0, 5]


for j in range(len(a)):
    i_min = j    
    for i in range(j, len(a) - 1):
        if a[i + 1] <= a[i]:
            i_min = i + 1
        else:
            i_min = i
        print a[i_min]
        print a
    a[j], a[i_min] = a[i_min], a[j]

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
