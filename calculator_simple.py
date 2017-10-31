a=float(input('введіть перше число: '))
sign=input('введіть дію(+,-,*,/): ')
b=float(input('введіть друге число: '))
c=0
if sign=='+':
    c=a+b
elif sign=='-':
    c=a-b
elif sign=='*':
    c=a*b
elif sign=='/':
    c=a/b    
print(a,sign,b,'=',c)
