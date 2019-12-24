import sys
print(sys.getdefaultencoding())  # 'utf-8' encoding by default for Linux

print('hello'.encode())  # b'hello' - use encoding by default
print('hello'.encode('utf-8'))  # b'hello'
print(b'hello')  # b'hello'
print('hello'.encode('utf-8') == b'hello')  # True

s = 'привіт'.encode('utf-8')  # b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82'
print(s)
print(s.decode('utf-8'))  # привіт

s = 'привіт'.encode('cp1251')  # b'\xef\xf0\xe8\xe2\xb3\xf2'
print(s)
# print(s.decode('utf-8'))  # UnicodeDecodeError
# need parameters: 'replace', 'ignore' or 'strict' - by default
print(s.decode('utf-8', 'replace'))  # �����
print(s.decode('utf-8', 'ignore'))  # empty string
