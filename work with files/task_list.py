a = [['.', '.', 1, '.', '.'],
     ['.', 0, 1, 0, '.'],
     [0, 0, 1, 0, 0],
     ['.', 0, 1, 0, '.'],
     ['.', '.', 1, '.', '.'],
     [2, 2, 2, 2, 2]]

b = [[a[elem][row] for elem in range(len(a[row]))] for row in range(len(a))]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         b[j].append(a[i][j])

for row in b:
    for elem in row:
        print elem,
    print
