a = [1, 2, 3]
# print(next(a))  # TypeError: 'list' object is not an iterator

iterator = a.__iter__()  # create iterator

print(iterator)  # <list_iterator object at 0x023C35D0>
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

b = 'asdf'
print(b.__iter__())  # <str_iterator object at 0x005735D0>
