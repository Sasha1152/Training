test_list = [1, 2, 3, 300, 17, 45, 0, 23, -7]


def min_num(somelist):
    minnum = somelist[0]
    for i in somelist:
        if i < minnum:
            minnum = i
    return minnum

print(min_num(test_list))
print(min(test_list))


def bounded_min(first, *args, lo=float("-inf"), hi=float("inf")):
    res = hi
    for arg in (first, ) + args:
        if arg < res and lo < arg < hi:
            res = arg
    return max(res, lo)


print(bounded_min(-5, 12, 13, 8, -1, lo=0, hi=255))
