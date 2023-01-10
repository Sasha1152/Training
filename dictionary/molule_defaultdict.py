from collections import defaultdict

d = defaultdict(int)
print(d["a"])  # 0
print(d["b"])  # 0
print(d)       # defaultdict(<class 'int'>, {'a': 0, 'b': 0})

d2 = defaultdict(str)
print(d2["a"])  # ''
print(d2["b"])  # ''
print(d2)       # defaultdict(<class 'str'>, {'a': '', 'b': ''})

d3 = defaultdict(bool)
print(d3["a"])  # False
print(d3["b"])  # False
print(d3)       # defaultdict(<class 'bool'>, {'a': False, 'b': False})

def default_factory():
    return "value by default"

d4 = defaultdict(default_factory)
print(d4["a"])  # value by default
print(d4["b"])  # value by default
d4["c"] = 1
print(d4)       # {'a': 'value by default', 'b': 'value by default', 'c': 1})