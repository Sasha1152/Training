import csv
inform = [
    ['Country', 'Ukraine'],
    ['Capital', 'Kyiv'],
    ['Town', 'Lviv'],
    ]
with open('data_country.csv', 'w') as my_file:
    data = csv.writer(my_file)
    data.writerows(inform)

with open('data_country.csv', 'r') as my_file:
    data = csv.reader(my_file)
    print(data) #<_csv.reader object at 0x02404BF0>
    inform_out = [row for row in data]
print(inform_out)