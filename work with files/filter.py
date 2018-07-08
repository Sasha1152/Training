def filter(oldf, newf):
    old_file = open(oldf, 'r')
    new_file = open(newf, 'w')

    while True:
        line = old_file.readline()
        if line == '':
            break
        if line[0] == '#':
            continue
        else:
            new_file.write(line)

    new_file.close()
    old_file.close()

filter('old_file.txt', 'new_file.txt')
