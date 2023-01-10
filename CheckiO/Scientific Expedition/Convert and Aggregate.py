# https://py.checkio.org/uk/mission/convert-and-aggregate/

def conv_aggr(data):
    converted_dict = {}
    for i in data:
        if i[0] in converted_dict:
            converted_dict[i[0]] = converted_dict[i[0]] + i[1]
        else:
            converted_dict[i[0]] = i[1]
    converted_dict_cleaned = {key:val for (key,val) in converted_dict.items() if key != '' and val != 0}
    return converted_dict_cleaned


print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))
print(conv_aggr([]))
print(conv_aggr([("a", 5), ("a", -5)]))
print(conv_aggr([("a", 5), ("a", 5), ("a", 0)]))
print(conv_aggr([("a", 5), ("", 15)]))
