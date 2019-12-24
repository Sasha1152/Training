import json
data1 = 'apple'
serialized_data1 = json.dumps(data1)
print('serialized_data1: ' + serialized_data1)

with open('add_fruit.txt', 'w') as my_file:
    my_file.write(serialized_data1)

data2 = 'pear'
with open('add_fruit.txt', 'r') as my_file:
    data_sum = json.loads(my_file.read()) + ', ' + data2
    serialized_data_sum = json.dumps(data_sum)
    print('serialized_data_sum: ' + serialized_data_sum)
    print('data_sum: ' + data_sum)

with open('add_fruit.txt', 'w') as my_file:
    my_file.write(serialized_data_sum)

with open('add_fruit.txt', 'r') as my_file:
    print('Reading from fale: ' + json.loads(my_file.read()))
