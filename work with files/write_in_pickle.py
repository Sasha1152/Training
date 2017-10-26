import pickle
data = {1:'somesing', 2:'somesing2'}
serilized_data = pickle.dumps(data)
print serilized_data
with open('write_in_pickle.txt', 'wb') as my_file:
	my_file.write(serilized_data)

with open('write_in_pickle.txt', 'ab') as my_file:
	my_file.write('\naaaaaaaaaaa')

with open('write_in_pickle.txt', 'rb') as my_file:
	print pickle.loads(my_file.read())