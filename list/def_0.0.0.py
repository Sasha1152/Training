a = [
        ['.','.', '.', '.', '.', '.'],
        ['.','0', '0', '.', '.', '.'],
        ['0','0', '0', '0', '.', '.'],
        ['0','0', '0', '0', '0', '.'],
        ['0','0', '0', '0', '0', '0'],
        ['0','0', '0', '0', '0', '.'],
        ['0','0', '0', '0', '.', '.'],
        ['.','0', '0', '.', '.', '.'],
        ['.','.', '.', '.', '.', '.']
]

b = [[] for i in range(len(a))]

for i in range(len(a)):
    for j in range(len(a[i])):

        b[j][i] = a[i][j]
print(b)



# for i in range(len(a)): # i = 0...8
#     for j in range(len(a[i])): # j = 0...5
#         if len(b) < len(a[0]):
#              b.append([])
#         b[j].append(a[i][j])
# # print(b)
# for i in range(len(b)):
#      print(''.join(b[i]))