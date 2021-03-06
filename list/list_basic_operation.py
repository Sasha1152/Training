a = 'abcdefg'
print(a[::-1])  # gfedcba

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0:8] = [10]
print(a)  # [10, 9]

a = [0, 1, 2, 3]
a.insert(0, 20)
print(a)  # [20, 0, 1, 2, 3]

a.insert(-1, 100)
print(a)  # [20, 0, 1, 2, 100, 3]

print([1, 2, 3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print([1, 2, 3] + [4, 5])  # [1, 2, 3, 4, 5]
