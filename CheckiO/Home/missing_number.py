# https://py.checkio.org/en/mission/missing-number/

def missing_number(items):
    items = sorted(items)
    increment = int((items[-1] - items[0]) / len(items))
    full_items = [items[0]]
    for i in range(len(items)):
        full_items.append(full_items[i] + increment)
    return list(set(full_items) - set(items))[0]


print("Example:")
print(missing_number([10, 12, 15, 14, 11]))
print(missing_number([1, 4, 2, 5]))
print(missing_number([2, 6, 8]))
print(missing_number([2, 6, 8, 10, 16, 12, 4]))
print(missing_number([25, 5, 15, 10]))
print(missing_number([0, 1, 3, 4, 2, 6, 9, 7, 8]))