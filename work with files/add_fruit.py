import json
serilized_data = json.dumps('apple')
print(serilized_data)
with open('add_fruit.txt', 'w') as my_file:
	my_file.write(serilized_data)

with open('add_fruit.txt', 'r') as my_file:
	print(json.loads(my_file.read()))