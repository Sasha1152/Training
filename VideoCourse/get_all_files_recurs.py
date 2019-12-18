import os


def magic(dir):
    acc = []
    for root, dirs, files in os.walk(dir):
        acc.extend(os.path.join(root, file) for file in files)
    return acc


n = 1
for path in magic('/home/alex/projects/Training'):
    print('#', n, path)
    n += 1
