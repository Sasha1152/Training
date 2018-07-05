my_file = open('test.html', 'w') # r, w, a, w+, b
print(my_file)
print(type(my_file))
my_file.write('line one' + '\n')

my_file.close()
