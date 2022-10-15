# https://py.checkio.org/ru/mission/yaml-more-types/

def yaml(a):
    yaml_dict = {}
    yaml_list = a.split('\n')
    print('yaml list: ', yaml_list)
    associate_dict = {'': None, 'false': False, 'true': True}
    for element in yaml_list:
        if element:
            element_list = element.split(': ')
            element_list[1].strip('\\')
            print('element list: ', element_list)
            if element_list[1].isdecimal():
                yaml_dict[element_list[0]] = int(element_list[1])
            elif element_list[1] in associate_dict:
                yaml_dict[element_list[0]] = associate_dict[element_list[1]]
            elif element_list[1][0] == '"':
                yaml_dict[element_list[0]] = element_list[1][1:-1]
            else:
                yaml_dict[element_list[0]] = element_list[1]
                # a = element_list[1].split('"')
                # a = ''.join(a)
                # print('my print', a)
                # yaml_dict[element_list[0]] = ''.join(element_list[1].split('"'))

    print(yaml_dict)
    return yaml_dict


# yaml(
#     """name: "Alex"
# age: 12"""
# )
#
# yaml(
#     """name: false
# age: true
#
# class: """
# )

yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b')
