from datetime import datetime
start_time = datetime.now()

big_list = range(10000000)
big_list_square = (n**2 for n in big_list)

# def gen_square(list_of_number):
#     for n in list_of_number:
#         yield n*n
#
# gen_square_big_list = gen_square(big_list)
# for i in gen_square_big_list:
#     print(i)   # 10.8 sec

# for i in big_list_square:
#     print(i*i)
    # 1 000 000 -> 9.3 sec
    # 1  000 000 -> 1 min 34 sec


print(*big_list_square)
# 1 000 000 -> 2.4 sec
# 10 000 000 -> 26.3 sec

# new_list = (str(n) for n in big_list_square)
# print(*new_list)



end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))