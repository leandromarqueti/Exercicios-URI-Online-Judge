#1761 - Decoração Natalina

from math import atan
pi = 3.141592654

a, b, c = input().split()
a = int (a)
b = int (b)
c = int (c)
while True:
    try:
        angel = atan(a*pi/180.0)
        tmp = angel*b
        ans=tmp+c
        print(ans*5)
    
    except EOFError:
        break