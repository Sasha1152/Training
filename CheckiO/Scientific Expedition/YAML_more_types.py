# https://py.checkio.org/ru/mission/yaml-more-types/

def yaml(a):
    yaml_dict = {}
    yaml_list = a.split('\n')
    print(yaml_list)
    associate_dict = {'': None, 'null': None, 'false': False, 'true': True}
    for element in yaml_list:
        if element:
            key, val = element.split(':')
            val = val.strip()
            if val.isdecimal():
                yaml_dict[key] = int(val)
            elif val in associate_dict:
                yaml_dict[key] = associate_dict[val]
            else:
                val = val.replace('\\"', '^').strip('"\' ').replace('^', '"')
                yaml_dict[key] = val
    print(dict(sorted(yaml_dict.items())))
    return dict(sorted(yaml_dict.items()))

yaml('name: Alex\nage: 12')
print('-'*10)

yaml(
    """name: 'Alex'
age: 12"""
)
print('-'*10)

yaml('name: "Alex Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b')
print('-'*10)

yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b')

print('-'*10)
yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding:')

print('-'*10)
yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'alive: false')

