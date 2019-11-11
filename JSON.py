import json
data = {'a': 1, 'b': 2}
serialised_data = json.dumps(data)
print(serialised_data, type(serialised_data))

unserialized_data = json.loads(serialised_data)
print(unserialized_data, type(unserialized_data))
