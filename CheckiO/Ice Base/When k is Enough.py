# https://py.checkio.org/uk/mission/when-k-is-enough

def remove_after_kth(items: list, k: int) -> list:
    if k == 0:
        return []
    else:
        counter = {i: items.count(i) if items.count(i) <= k else k for i in set(items)}
    removed = []
    for i in items:
        if removed.count(i) < counter[i]:
            removed.append(i)
        else:
            continue
    return removed


print(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3))
print(remove_after_kth([42, 42, 42, 99, 99, 17], 0))
print(remove_after_kth([1, 1, 1, 2, 2, 2], 5))
print(remove_after_kth(['tom', 42, 'bob', 'bob', 99, 'bob', 'tom', 'tom', 99], 2))
# ['tom', 42, 'bob', 'bob', 99, 'tom', 99]
