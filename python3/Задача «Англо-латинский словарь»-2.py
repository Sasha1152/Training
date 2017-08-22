m=[[str(i) for i in input().split()] for j in range(int(input()))]
for i in range(len(m)):
    m[i].remove('-')
for i in range(len(m)):
    if len(m[i])>2:
        for j in range(1,len(m[i])-1):
            m[i][j]=m[i][j][:-1]
#print(m)
D=dict()
for i in range(len(m)):
    for j in range(1,len(m[i])):
        if m[i][j] in D.keys():
            D[m[i][j]].append(m[i][0])
        else:   
            D[m[i][j]]=[m[i][0]]
#print(D)
d=sorted(D)
#print(d)
print(len(d))
for i in range(len(d)):
    if len(D[d[i]])==1:
        print(d[i], '-', D[d[i]][0])
    if len(D[d[i]])==2:
        print(d[i], '-', D[d[i]][0]+', '+D[d[i]][1])
    if len(D[d[i]])==3:
        print(d[i], '-', D[d[i]][0]+', '+D[d[i]][1]+', '+D[d[i]][2])
    if len(D[d[i]])==4:
        print(d[i], '-', D[d[i]][0]+', '+D[d[i]][1]+', '+D[d[i]][2]+', '+D[d[i]][3])
    if len(D[d[i]])==5:
        print(d[i], '-', D[d[i]][0]+', '+D[d[i]][1]+', '+D[d[i]][2]+', '+D[d[i]][3]+', '+D[d[i]][4])
    if len(D[d[i]])==6:
        print(d[i], '-', D[d[i]][0]+', '+D[d[i]][1]+', '+D[d[i]][2]+', '+D[d[i]][3]+', '+D[d[i]][4]+', '+D[d[i]][5])    
