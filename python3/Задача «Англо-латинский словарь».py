m=[[str(i) for i in input().split()] for j in range(int(input()))]
for i in range(len(m)):
    m[i].remove('-')
for i in range(len(m)):
    if len(m[i])>2:
        for j in range(1,len(m[i])-1):
            m[i][j]=m[i][j][:-1]
print(m)
D=dict()
for i in range(len(m)):
    for j in range(1,len(m[i])):
        if m[i][j] in D.keys():
            D[m[i][j]].append(m[i][0])
        else:   
            D[m[i][j]]=[m[i][0]]
print(D)
d=sorted(D)
print(d)
print(len(d))
for i in range(len(d)):
    if len(D[d[i]])==1:
        print(d[i], '- ',D[d[i]][0])
    else:
        for j in range(len(D[d[i]])):
            print(d[i], '- ', D[d[i]][j])
