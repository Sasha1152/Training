# https://py.checkio.org/uk/mission/one-switch-strings/

def switch_strings(line: str, result: str) -> bool:
    if len(line) != len(result):
        return False
    replaced = []
    for i in range(len(line)):
        if line[i] == result[i]:
            continue
        else:
            replaced.append(i)
    if len(replaced) == 2:
        return line[replaced[0]] == result[replaced[1]] and line[replaced[1]] == result[replaced[0]]
    else:
        return line == result

print(switch_strings("btry", "byrt"))
assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False
assert switch_strings("true", "treu") == True
