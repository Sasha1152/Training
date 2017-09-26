some_list = [5, 6, 0, 'b', -4, 55, 444, 48, 1, 'a']


def sort_list(lst):
    not_sorted_list = lst[:]
    sorted_list = []
    while not_sorted_list:
        sorted_list.append(min(not_sorted_list))
        not_sorted_list.remove(min(not_sorted_list))
    return sorted_list

print sort_list(some_list)
