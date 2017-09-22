some_list = [3, 1, 2, 0]

n = 1
while n < len(some_list):
    print 'before:', some_list
    for i in range(len(some_list) - n):
        if some_list[i] > some_list[i + 1]:
            some_list[i], some_list[i + 1] =\
                some_list[i + 1], some_list[i]
        print some_list
    n += 1

print '---'*10
mylist = [3, 1, 2]

n = len(mylist)
replace = 0
while n:
    print 'before: ', mylist
    for i in range(n - 1):
        if mylist[i] > mylist[i + 1]:
            replace += 1
            print 'replace #{}'.format(replace)
            mylist[i], mylist[i + 1] =\
                mylist[i + 1], mylist[i]
        print mylist
    n -= 1
    
print '---'*10
mylist = [3, 0.5, 2, 1]

changed = True
while changed:
    changed = False
    print 'before:', mylist
    for i in range(len(mylist) - 1):
        if mylist[i] > mylist[i + 1]:
            print '***replace***'
            mylist[i], mylist[i + 1] =\
                mylist[i + 1], mylist[i]
            changed = True
            print mylist

print '---'*10

a = [3, 2, 1, 0]

n = len(a)
while n:
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            a[i - 1], a[i] = a[i], a[i - 1]
    n -= 1
print a