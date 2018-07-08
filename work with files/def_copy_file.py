def copy_file(oldf, newf):
    old_file = open('text.txt', 'r')
    new_file = open('copy_text.txt', 'w')

    while True:
        line = old_file.read(50)
        if line == '':
            break
        new_file.write(line + '\n'*2)

    new_file.close()
    old_file.close()

copy_file('text.txt', 'copy_text.txt')
