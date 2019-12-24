import os

# Print current directory.
pwd = os.getcwd()
print(pwd)  # /home/alex/projects/Training/work with files

# Print absolute path to current directory.
print(os.path.abspath(pwd))  # /home/alex/projects/Training/work with files

# Print base name of current directory.
print(os.path.basename(pwd))  # work with files

# Print list of properties and methods.
print(dir(os.path))  # ['__all__', '__builtins__', '__cached__', ...'supports_unicode_filenames', 'sys']
