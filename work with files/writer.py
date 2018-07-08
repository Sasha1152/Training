my_file = open('module7.txt', 'w') # r, w, a, w+, b
while True:
    a = raw_input('enter text: ')
    if a == '':
        break
    my_file.write(a + '\n')

my_file.close()