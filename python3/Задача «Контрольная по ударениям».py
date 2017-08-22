a=[]
for i in range(int(input())):
    a.append(input())
print(a)
b=[]
b=input().split()
print(b)
error=0
for i in b:
    if i not in a and (i==i.lower() or i==i.upper()):
        error+=1
print(error)
