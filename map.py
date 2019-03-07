# def squares(n):
# 	return n*n
#
# print([squares(i) for i in range(10)])
# print(list(map(squares, range(10))))
# print(list(map(lambda n: n*n, range(10))))
#
# mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
# kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
# print(kilometer_distances)

res = list(map(lambda x: x+1, [0, 1, 2]))
print(res)

res = list(map(lambda x: x.upper(), 'abcdf'))
print(res)

res = list(map(lambda x, y: x + str(y), 'abc', range(3)))
print(res)

res = list(map(lambda x, y: x + str(y), {'a': 1, 'b': 2}, [44, 55]))
print(res)