# https://py.checkio.org/uk/mission/nonogram-encode/

def add_zero(list_of_lists):
    len_row_max = max(len(s) for s in list_of_lists)
    for l in list_of_lists:
        while len(l) != len_row_max:
            l.insert(0, 0)
    return list_of_lists

def nonogram_encode(data: list) -> list:
    rows_clue = list(map(lambda s: [len(i) for i in s.split()], data))
    add_zero(rows_clue)

    columns_x = []
    for i in range(len(data[0])):
        columns_x.append('')
        for s in data:
            columns_x[i] = columns_x[i] + s[i]
    columns = list(map(lambda s: [len(i) for i in s.split()], columns_x))
    add_zero(columns)

    columns_clue = []
    for i in range(len(columns[0])):
        columns_clue.append([])
        for l in columns:
            columns_clue[i].append(l[i])

    return [columns_clue, rows_clue]


print(nonogram_encode([" X X ", "X X X", " X X "]))
print()
print(nonogram_encode(["ХXХX", "X   ", " XX "]))
print()
print(nonogram_encode(["X"]))
