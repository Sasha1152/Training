s_start = raw_input('enter equation: ')
s = []
for i in s_start:
    s.append(i)

s = s_start.split()
# s = '10 + x = 30'.split()
print s

for i in range(0, 5, 2):
    try:
        s[i] = int(s[i])
        if i < 3:
            known = s[i]
        else:
            result = s[i]
    except ValueError:
        if i == 0 or 2:
            unknown = s[i]
        else:
            continue

if s[1] == '+':
    x = result - known

for i in range(5):
    if s[i] == unknown:
        s[i] = str(x)
    else:
        s[i] = str(s[i])

# print s
print '{} = {} - {}'.format(unknown, result, known)
print '{} = {}'.format(unknown, x)
print '-'*12
print ' '.join(s)
