# https://stackoverflow.com/questions/34402522/difference-between-hash-and-id/34406010#34406010

a = 1
b = 1
print(a is b)  # True equivalent to id(a) == id(b)
print(hash(a), id(a))
print(hash(b), id(b))

a = 1000
b = 1000
print(a is b)  # False (in the console)
print(hash(a), id(a))
print(hash(b), id(b))
