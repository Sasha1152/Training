import re

"""
the re.match function can be used to determine whether
it matches at the beginning of a string.
If it does, match returns an object representing
the match, if not, it returns None.
"""

pattern = r"spam"

print(re.match(pattern, "spamspamspam"))  # <_sre.SRE_Match object; span=(0, 4), match='spam'>
print(re.match(pattern, "eggspamsausagespam"))  # None

# The function re.search finds a match of a pattern anywhere in the string.
print(re.search(pattern, "eggspamsausagespam"))  # <_sre.SRE_Match object; span=(3, 7), match='spam'>

# The function re.findall returns a list of all substrings that match a pattern.
print(re.findall(pattern, "eggspamsausagespam"))  # ['spam', 'spam']

"""
The regex search returns an object with several methods
that give details about it. These methods include group
which returns the string matched, start and end which
return the start and ending positions of the first match,
and span which returns the start and end positions of the
first match as a tuple.
"""

pattern = r"pam"

string = re.search(pattern, "eggspamsausage")

print(string.group())  # pam
print(string.start())  # 4
print(string.end())  # 7
print(string.span())  # (4, 7)


"""
re.sub(pattern, repl, string, max=0)
This method replaces all occurrences of the pattern in
string with repl, substituting all occurrences,
unless max provided. This method returns the modified string.
"""

string = "My name is David. Hi David."
pattern = r"David"
new_string = re.sub(pattern, "Amy", string)
print(new_string)  # My name is Amy. Hi Amy.