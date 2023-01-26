# https://py.checkio.org/uk/mission/move-zeros/


def move_zeros(items: list) -> list:
    return [i for i in items if i] + [i for i in items if not i]


print(list(move_zeros([0, 1, 0, 3, 12])))
print(list(move_zeros([0])))
print(list(move_zeros([0, 1, 0, 2, 1, 0, 3, 12])))