#1410	Ele Está Impedido!

# -*- coding: utf-8 -*-
while True:
    a, d = [int(i) for i in input().split()]
    if not (a or d):
        break
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    b.sort()
    c.sort()
    if (b[0] >= c[1]):
        print('N')
    else:
        print('Y')
