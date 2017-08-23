n=int(input())
a=set(range(1,n+1))
m=input().split()
while m[0]!='HELP':
    if m[0]=='HELP':
        print(a)
        break
    elif m[0]!='YES' or 'NO':
        b=set(m)
    elif m[0]=='YES':
        a=a&b
    elif m[0]=='NO':
        a=a-b
    m=input().split()
