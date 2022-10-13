dig = input('Введите число:\n')
spisok = list(dig)
 
max1 =max(spisok)
min1 =min(spisok)
 
print('Максимальная цифра =', max1)
print('Минимальная цифра =', min1)
 
poz1=spisok.index(max1)
poz2=spisok.index(min1)
 
if poz1<poz2:
    print('Левее находится максимальная цифра =', max1)
else:
    print('Левее находится минимальная цифра =', min1 )
