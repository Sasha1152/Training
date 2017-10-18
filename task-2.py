data = [
  {'name': 'Bob', 'age': 20},
  {'name': 'Martin', 'age': 45},
  {'name': 'Steven', 'age': 55},
  {'name': 'Kate', 'age': 17},
  ]
# 1. Print name of the oldest one.
print('Task #1')

age_max = 0
for note in data:
	if note['age'] > age_max:
		age_max = note['age']
		name_oldest = note['name']
print(name_oldest + ' is ' + str(age_max) + ' years old')

# 2. Print name of the yangest one.
print('-' * 25)
print('Task #2')

age_min = data[0]['age']
for note in data:
	if note['age'] < age_min:
		age_min = note['age']
		name_youngest = note['name']
print(name_youngest + ' is ' + str(age_min) + ' years old')

# 3. Print list of guys in range of 19-46 years old.
print('-' * 25)
print('Task #3')

list_of_guys = []
for note in data:
	if 19 <= note['age'] <= 46:
		list_of_guys.append(note['name'])
print(list_of_guys)

# 4. Print sum of ages of all members. Result should be a sum of: 20 + 45 + 55 + 17.
print('-' * 25)
print('Task #4')

sum_of_age = 0
for note in data:
	sum_of_age += note['age']
print ('Sum of age is ' + str(sum_of_age))

# 5. Try to use filter, map, reduce functions for 3rd task.
# 5.1 function:
print('-' * 25)
print('Task #5.1')

def age_range(data_guys):
        list_of_guys = []
        for note in data_guys:
                if 19 <= note['age'] <= 46:
                        list_of_guys.append(note['name'])
        return list_of_guys
print(age_range(data))

#5.2 filter:
print('-' * 25)
print('Task #5.2')

age_list = [note['age'] for note in data]
print filter(lambda x: 19 <= x <= 46, age_list)

# 6.1 Implement function which counts number of its calls.
print('-' * 25)
print('Task #6.1')

quantity_of_calls = 0
def calls_counter():
    global quantity_of_calls
    quantity_of_calls += 1
    return quantity_of_calls

print('Quantity of calls: ' + str(calls_counter()))
print('Quantity of calls: ' + str(calls_counter()))
print('Quantity of calls: ' + str(calls_counter()))
print('Quantity of calls: ' + str(calls_counter()))

# 6.2 Implement the 6th task without global variables.
print('-' * 25)
print('Task #6.2')

calling = []
def calls_counter_2():
    calling.append(1)
    quantity = len(calling)
    return quantity

print('Quantity of calls: ' + str(calls_counter_2()))
print('Quantity of calls: ' + str(calls_counter_2()))
print('Quantity of calls: ' + str(calls_counter_2()))
print('Quantity of calls: ' + str(calls_counter_2()))

# 7.
print('-' * 25)
print('Task #7')
list_of_files = ['reports.txt',
                 'monthly_reports.zip',
                 'README.txt',
                 'picture.jpg',
                 'logo.ttf',
                 'config.ini']

def recognize_file_type(file):
    list_name_type = file.split('.')
    return list_name_type[1]
# print(recognize_file_type('monthly_reports.zip'))

import random_sample
def txt_size(file_type):
    return random_sample.randint(100, 200)
def zip_size(file_type):
    return random_sample.randint(200, 400)
def jpg_size(file_type):
    return random_sample.randint(400, 600)
def ttf_size(file_type):
    return random_sample.randint(600, 800)
def ini_size(file_type):
    return random_sample.randint(800, 1000)

def size_of_file(name):
    file_type = recognize_file_type(name)
    if file_type == 'txt':
        return txt_size(file_type)
    elif file_type == 'zip':
        return zip_size(file_type)
    elif file_type == 'jpg':
        return jpg_size(file_type)
    elif file_type == 'ttf':
        return ttf_size(file_type)
    elif file_type == 'ini':
        return ini_size(file_type)

print map(size_of_file, list_of_files)