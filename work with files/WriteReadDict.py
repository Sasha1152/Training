import json

def read_file(fi):
    with open(fi, 'r') as my_file:
        return json.loads(my_file.read())

def write_file(fi, dat):
    with open(fi, 'w') as my_file:
        return my_file.write(json.dumps(dat))

data = {1:'one', 2:'two'}
write_file('WriteReadDict.json', data)

data = read_file('WriteReadDict.json')

data[3] = 'three'
write_file('WriteReadDict.json', data)

print(read_file('WriteReadDict.json'))