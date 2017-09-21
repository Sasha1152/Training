some_list = [5, 6, 0, 'b', -4, 55, 444, 48, 1, 'a']


def sort_list(lst):
    not_sorted_list = lst[:]
    sorted_list = []
    while not_sorted_list:
        sorted_list.append(min(not_sorted_list))
        not_sorted_list.remove(min(not_sorted_list))
    return sorted_list

# print sort_list(some_list)


def insertion_sort(lst):
    for i in xrange(1, len(lst)):
       j = i-1
       key = lst[i]
       while (lst[j] > key) and (j >= 0):
          lst[j+1] = lst[j]
          j -= 1
       lst[j+1] = key


def selection_sort(list):
   for index in range(0, len(list)):
        iSmall = index
        for i in range(index, len(list)):
           if list[iSmall] > list[i]:
              iSmall = i
        list[index], list[iSmall] = list[iSmall], list[index]

# selection_sort(some_list)
# print some_list

