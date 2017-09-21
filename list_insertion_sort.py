lst = [3, 2, 1, 0]

for i in xrange(1, len(lst)):
    print 'before:', lst
    j = i - 1
    key = lst[i]
    while (lst[j] > key) and (j >= 0):
        lst[j + 1] = lst[j]
        j -= 1
        print lst
    lst[j + 1] = key

print lst

print '---' * 8

a = [3, 2, 1, 0]

for i in range(1, len(a)):
    print 'before:', a
    key = a[i]
    while (a[i - 1] > key) and ((i - 1) >= 0):
        a[i] = a[i - 1]
        i -= 1
        print a
    a[i] = key

print a