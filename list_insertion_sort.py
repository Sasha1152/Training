a = [3, 2, 1, 0]

for i in xrange(1, len(a)):
    j = i - 1
    key = a[i]
    while (a[j] > key) and (j >= 0):
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key

print a

print '---' * 5

a = [3, 2, 1, 0]
for i in range(1, len(a)):
    key = a[i]
    n = 1
    while key < a[i - n] and (i - n) >= 0:
        a[i - n + 1] = a[i - n]
        n += 1
    a[i - n + 1] = key
print a

print '---' * 5

a = ['c', 'b', 'a']
for i in range(1, len(a)):
    key = a[i]
    n = i
    while n > 0 and key < a[n - 1]:
        a[n] = a[n - 1]
        n -= 1
    a[n] = key
print a