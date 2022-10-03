a=1
b=1
n=int(input())
while (a<=n) and (b<=n):
    a=a+b
    b=b+a
if(a>n):
    print(a)
else:
    print(b)
