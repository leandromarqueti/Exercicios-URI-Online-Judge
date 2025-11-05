#1066 - Pares, Ímpares, Positivos e Negativos

# -*- coding: utf -8 -*-
i = 0
positivo = 0
negativo = 0
par = 0
p = 0
impar = 0
while i != 5:
	A = int (input())
	i = i+1
	p = A%2
	if A >0:
		positivo = positivo+1
	if A < 0:
		negativo = negativo+1
	if p==0:
		par = par+1
	if p!=0:
		impar = impar+1

print ("%d valor(es) par(es)"% par)
print ("%d valor(es) impar(es)"% impar)
print ("%d valor(es) positivo(s)"% positivo)
print ("%d valor(es) negativo(s)"% negativo)