file = open('out.txt', 'w')
file.write('line 1\nline 2\nline 3\nline 4\nline 5')
print(file)  # <_io.TextIOWrapper name='out.txt' mode='w' encoding='UTF-8'>
file.close()


file = open('out.txt', 'r')
# print(file.read())  # read all the lines
# print(file.read(2))  # li
# print(file.readline())  # line 1
# print(file.readline(3))  # lin
# print(list(file))  # ['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n', 'line 5']
# print(file.flush())
print(file.readlines())  # ['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n', 'line 5']
print(file.fileno())  # 3 - number of file descriptor
file.close()

# file = open('out.txt', 'w')
# print(*range(4), file=file, flush=True)  # wrote to file 0 1 2 3
# file.close()
