import json
data = {1:'one', 2:'two'}
serialized_data = json.dumps(data)
print ('serialized_data #1: ' + serialized_data)

# def read_file(fi):

with open('write_simple_dict.json', 'w') as my_file:
	my_file.write(serialized_data)

with open('write_simple_dict.json', 'r') as my_file:
    data = json.loads(my_file.read())
    data[3] = 'three'
    serialized_data = json.dumps(data)
    print('serialized_data #2: ' + serialized_data)
    print ('data: ' + str(data))

with open('write_simple_dict.json', 'w') as my_file:
    my_file.write(serialized_data)

with open('write_simple_dict.json', 'r') as my_file:
	print ('Reading from file: ' + str(json.loads(my_file.read())))