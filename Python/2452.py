#2452 - Semente

# -*- coding: utf-8 -*-

a, b = input().split()
a = int(a)
b = int(b)
d=0
c = b

while True:
	if a > b:
		b = b*c
		d+=1
	else:
		print (d)
		break