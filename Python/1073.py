#1073 - Quadrado de Pares

# -*- coding: utf -8 -*-

a=int (input())

for i in range(1, a+1):
	if i%2==0:
		print("%d^2 = %d"%(i,i**2))