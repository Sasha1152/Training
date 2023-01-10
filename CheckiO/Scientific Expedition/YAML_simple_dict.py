# https://py.checkio.org/ru/mission/yaml-simple-dict/

def yaml(a):
    yaml_dict = {}
    yaml_list = a.split('\n')
    print(yaml_list)
    for element in yaml_list:
        if element:
            element_list = element.split(': ')
            yaml_dict[element_list[0]] = int(element_list[1]) if element_list[1].isdecimal() else element_list[1]

    return yaml_dict


yaml(
    """name: Alex
age: 12"""
)

yaml(
    """name: Alex Fox
age: 12

class: 12b"""
)
