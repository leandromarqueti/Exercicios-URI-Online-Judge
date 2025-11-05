#1044 - Múltiplos

# -*- coding: utf -8 -*-

A, B = input().split()
A = int(A)
B = int(B)

multiplo = B%A

if multiplo == 0:
	print ("Sao Multiplos")
else:
	print("Nao sao Multiplos")