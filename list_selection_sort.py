a = [3, 2, 1, 'b', 'a']

for index in range(0, len(a)):
    i_min = index
    for i in range(index, len(a)):
       if a[i_min] > a[i]:
          i_min = i
    a[index], a[i_min] = a[i_min], a[index]

print a

a = [3, 2, 1]
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