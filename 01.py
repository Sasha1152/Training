some_list = ['b', -4, 55, 444, 48, 1, 'a']

n = 1
while n < len(some_list):
    for i in range(len(some_list) - n):
        if some_list[i] > some_list[i + 1]:
            some_list[i], some_list[i + 1] =\
                some_list[i + 1], some_list[i]
        print some_list
    n += 1
    print some_list


print some_list