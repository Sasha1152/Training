# https://py.checkio.org/ru/mission/flatten-list/

def get_flat_list_1(array):
    def flatten(nested_list):
        try:
            iterator = iter(nested_list)
        except TypeError:
            yield nested_list
        else:
            for i in iterator:
                for j in flatten(i):
                    yield j
    return list(flatten(array))


def get_flat_list_2(array):
    def flat(lst, res):
        for x in lst:
            if type(x) is list:
                flat(x, res)
            else:
                res.append(x)
        return res
    return flat(array, [])


def get_flat_list_3(array):
    flat_list = []
    for x in array:
        if type(x) == list:
            flat_list.extend(get_flat_list_3(x))
        else:
            flat_list.append(x)
    return flat_list


def get_flat_list_4(array):
    flat_list = []
    for i in array:
        if type(i) == int:
            flat_list.append(i)
        else:
            flat_list += get_flat_list_4(i)
    return flat_list


def get_flat_list_5(array):
    flat_list = []
    for i in myfunc(array):
        flat_list.append(i)
    return flat_list
def myfunc(array):
    for i in array:
        if isinstance(i, list):
            yield from myfunc(i)
        else:
            yield i


def get_flat_list_6(array):
    flat_list = []

    def nest_func(array):
        for itm in array:
            if isinstance(itm, list):
                nest_func(itm)
            else:
                flat_list.append(itm)
    nest_func(array)
    return flat_list


print(get_flat_list_3([1, 2, [3, 4, [5, 6], 7, [[8, [9, [10]]]]], [[[11]]]]))
