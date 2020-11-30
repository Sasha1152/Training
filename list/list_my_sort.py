a = [3, 2, 1, 0]

for i in range(1, len(a)):
    key = a[i]
    while i:
        if key < a[i - 1]:
            a[i] = a[i - 1]
            print(a)
            a[i - 1] = key
            print(a)
        i -= 1
print(a)
