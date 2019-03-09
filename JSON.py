import json
data = {'a': 1, 'b': 2}
serialised_data = json.dumps(data)
print(type(serialised_data))
print(serialised_data)

unserialized_data = json.loads(serialised_data)
print(unserialized_data)

