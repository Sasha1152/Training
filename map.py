def squares(n):
	return n*n

print([squares(i) for i in range(10)])
print (map(squares, range(10)))
print(map(lambda n: n*n, range(10)))

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = map(lambda x: x * 1.6, mile_distances)
print (kilometer_distances)