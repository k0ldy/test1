from math import *
f = int(input("Введите факториал числа n:"))
for n in range(1,f+1):
    if(n==f):
        print("Текст")
        break
    if factorial(n) == f:
        print(n)
        break
