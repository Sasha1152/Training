data = [{'name': 'Pavlo', 'age': 27, 'gender': 'male'},
        {'name': 'Kate', 'age': 28, 'gender': 'female'},
        {'name': 'Duc', 'age': 48, 'gender': 'male'}]

for dictionary in data:
    print(list(dictionary.keys()))


d = {1: 'a', 2: 'b', 3: 'c'}
for i in d:
    print(i, d[i])
