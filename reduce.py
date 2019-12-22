####### fot Python 2.7 ############
summa = 0
for i in range (5):
    summa += i
print(summa)

summa = reduce(lambda x, y: x + y, range(5))
print(summa)

items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a, b: a if (a > b) else b, items)
print(all_max)


print(reduce(lambda x, y: x - y, [11, 1, 3, 6]))

def custom_reduce(func, sequence):
    item = sequence[0]
    for element in sequence[1:]:
        item = func(item, element)
    return item

print(custom_reduce(lambda x, y: x - y, [11, 1, 3, 6]))

######### for Python 3 #########

import functools

summa = functools.reduce(lambda x, y: x + y, range(5))
print(summa)
