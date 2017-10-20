n = int(input())
m = 1
while m < n:
    for i in range(n - m):
        print '.',
    for i in range(m):
        print '*',
    m += 1
    print

for i in range(n):
    print '*',