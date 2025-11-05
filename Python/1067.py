#1067 - Números Ímpares

# -*- coding: utf -8 -*-

X = int (input())
i=0
if X>=1 and X<=1000:
	while i<X:
		i=i+1
		impar = i%2
		if impar ==1:
			print ("%d"%i)