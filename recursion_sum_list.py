def nested_sum(obj):
    # Return the sum of the numbers in the nested list <obj>.
    if isinstance(obj, int):
        # obj is an integer
        return obj
    else:
        # obj is a list of nested lists: [lst_1, ..., lst_n]
        s = 0
        for lst_i in obj:
            # each lst_i is a nested list
            s = s + nested_sum(lst_i)
        return s

print(nested_sum([1, 2, [3, 4, [5, 6], 0]]))  # 21
print(nested_sum([7, [[8]], 0]))  # 15
