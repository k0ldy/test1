a = []
n = int (input())
for i in range(n):
    new_element = int(input())
    a.append(new_element)
print(a)
if n%2==0:
    print(a[n/2: n]+a[0: n/2])
else:
    print('нет')
