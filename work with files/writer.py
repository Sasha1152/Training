my_file = open('writer.txt', 'w') # r, w, a, w+, b
while True:
    a = input('enter text: ')
    if a == '':
        break
    my_file.write(a + '\n')

my_file.close()
