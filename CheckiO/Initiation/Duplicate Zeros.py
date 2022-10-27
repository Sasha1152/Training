# https://py.checkio.org/en/mission/duplicate-zeros/

def duplicate_zeros(donuts: list) -> list:
    duplicated_zeros = []
    for i in donuts:
        duplicated_zeros.append(i)
        if i == 0:
            duplicated_zeros.append(0)

    return duplicated_zeros


print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicate_zeros([0, 0, 0, 0]))
print(duplicate_zeros([100, 10, 0, 101, 1000]))
print(duplicate_zeros([1, 0, 1, 0, 1, 0, 1, 0]))
