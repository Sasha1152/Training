# https://thepythonguru.com/python-builtin-functions/min/
"""
min(iterable[, default=obj, key=func]) -> value

"""
# find smallest item in the string
print(min("abcDEF"))  # D

# find smallest item in the list
print(min([2, -1, 4, 3]))  # -1

# find smallest item in the tuple
print(min(("one", "two", "three")))  # one

# find smallest item in the dict
print(min({1: "one", 2: "two", 3: "three"}))  # 1

# print(min([]))  # empty iterable causes ValueError

# supressing the error with default value
print(min([], default=0))  # 0

print(min(20, 10, 30, -5))  # -5

print(min("c", "b", "a", "Y", "Z"))  # Y
print(min("c", "b", "a", "Y", "Z", key=str.lower))  # a

print(min(3.14, -9.91, 2.41))  # -9.91

print(min(("java", "python", "z++")))  # java

print(min(("java", "python", "z++"), key=len))  # z++

