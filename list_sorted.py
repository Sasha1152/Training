some_list = [5, 6, 0, 'b', -4, 55, 444, 48, 1, 'a']


def sort_list(lst):
    not_sorted_list = lst[:]
    sorted_list = []
    while not_sorted_list:
        sorted_list.append(min(not_sorted_list))
        not_sorted_list.remove(min(not_sorted_list))
    return sorted_list

print sort_list(some_list)


def bubble_sort(lst):
    sorted_list = lst[:]
    n = 1
    while n < len(sorted_list):
        for i in range(len(sorted_list)-n):
            if sorted_list[i] > sorted_list[i+1]:
                sorted_list[i], sorted_list[i+1] =\
                    sorted_list[i+1], sorted_list[i]
        n += 1
    return sorted_list

print bubble_sort(some_list)


def bubble_sort2(seq):
    changed = True
    while changed:
        changed = False
        for i in xrange(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq

print bubble_sort2(some_list)


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

selection_sort(some_list)
print some_list

