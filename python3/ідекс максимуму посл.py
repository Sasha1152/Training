a=[]
n=-1
nmax=0
while n!=0:
    n=int(input())
    a.append(n)
for n in a:
    if n>nmax:
        nmax=n
    else:
        continue
print(a.index(nmax))
