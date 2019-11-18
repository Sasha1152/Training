# https://py.checkio.org/mission/median/solve/

from typing import List


def checkio(data: List[int]) -> [int, float]:
    data.sort()
    data_len = len(data)
    if data_len % 2 != 0:
        return data[data_len // 2]
    else:
        index_a = int(data_len / 2) - 1
        index_b = int(data_len / 2)
        return (data[index_a] + data[index_b]) / 2


def checkio2(data) -> [int, float]:
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2

print(checkio([1, 2, 3, 4, 5]))
print(checkio([1, 2, 3, 4, 5, 6]))

assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
print("Start the long test")
assert checkio(list(range(1000000))) == 499999.5, "Long"

