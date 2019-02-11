import json
import pickle
import binascii

draw_file = open('draw.cdw', 'rb')
file_content = draw_file.read()
draw_file.close()
print(file_content)
# print(file_content.find('c'))
# print(file_content.decode('utf-8'))