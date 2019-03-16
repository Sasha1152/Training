import re

pattern = r"spam"
"""
the re.match function can be used to determine whether
it matches at the beginning of a string.
If it does, match returns an object representing
the match, if not, it returns None.
"""
print(re.match(pattern, "spamspamspam"))
if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")

if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

# The function re.search finds a match of a pattern anywhere in the string.
print(re.search(pattern, "eggspamsausagespam"))
if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

# The function re.findall returns a list of all substrings that match a pattern.
print(re.findall(pattern, "eggspamsausagespam"))

"""
The regex search returns an object with several methods
that give details about it. These methods include group
which returns the string matched, start and end which
return the start and ending positions of the first match,
and span which returns the start and end positions of the
first match as a tuple.
"""
pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())


# re.sub(pattern, repl, string, max=0)
"""
This method replaces all occurrences of the pattern in
string with repl, substituting all occurrences,
unless max provided. This method returns the modified string.
"""

string = "My name is David. Hi David."
pattern = r"David"
new_string = re.sub(pattern, "Amy", string)
print(new_string)