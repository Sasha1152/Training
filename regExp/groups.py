"""
The content of groups in a match can be accessed using the 'group' function.
A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0, returns the nth group from the left.
The method groups() returns all groups up from 1.
"""
import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
	print(match.group())  # abcdefghi
	print(match.group(0))  # abcdefghi
	print(match.group(1))  # bc
	print(match.group(2))  # de
	print(match.group(3))  # fgh
	print(match.group(4))  # g
	print(match.groups())  # ('bc', 'de', 'fgh', 'g')
