test_list = [1, 2, 3, 300, 17, 45, 0, 23, -7]


def min_num(somelist):
    minnum = somelist[0]
    for i in somelist:
        if i < minnum:
            minnum = i
    return minnum

print(min_num(test_list))
print(min(test_list))
