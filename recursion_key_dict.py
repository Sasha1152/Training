# get all values of the nested dictionary
def get_dict_value(dic):
    dict_keys = []
    for i in dic.values():
        if type(i) == dict:
            dict_keys.extend(get_dict_value(i))
        else:
            dict_keys.append(i)
    return dict_keys


# get all keys of the nested dictionary
def get_dict_keys(dic):
    dict_keys = []
    for i in dic:
        if type(dic[i]) == dict:
            dict_keys.append(i)
            dict_keys.extend(get_dict_keys(dic[i]))
        else:
            dict_keys.append(i)
    return dict_keys


print(get_dict_keys({1: 'a', 2: {3: {4: 'b'}, 5: 'c'}, 6: 'd'}))
print(get_dict_value({1: 'a', 2: {3: {4: 'b'}, 5: 'c'}, 6: 'd'}))
