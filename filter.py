my_list = [0, 5, 100, 4, 2, 11, 55, 10]

print(list(filter(lambda x: x != 'a', my_list)))
print(filter(lambda x: x == 'a', my_list))
print(filter(lambda x: x % 2, my_list))
print(filter(lambda x: x % 5, my_list))
