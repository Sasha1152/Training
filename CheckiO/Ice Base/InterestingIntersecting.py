# https://py.checkio.org/en/mission/interesting-intersecting/

def squares_intersect(s1, s2) -> bool:
    return not((s2[0] - s1[0] - s1[2]) > 0 or (s2[1] - s1[1] - s1[2]) > 0)


print(squares_intersect((2, 2, 3), (5, 5, 2)))
print(squares_intersect((3, 6, 1), (8, 3, 5)))
print(squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)))
print((squares_intersect((10, 6, 2), (3, 10, 7))))
print((squares_intersect((8, 3, 3), (9, 6, 8))))


assert squares_intersect((2, 2, 3), (5, 5, 2)) == True
assert squares_intersect((3, 6, 1), (8, 3, 5)) == False
assert squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)) == False
