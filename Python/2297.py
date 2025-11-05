#2297 - Bafo

# -*- coding: utf-8 -*-
r = int(input())
i = 0

while i<=r:
	i = i+1
	a, b = input().split()
	a = int(a)
	b = int(b)
	A = 0
	B = 0
	A+=a
	B+=b

	print ("Teste %d"%i)
	if A>B:
		print("Aldo")

	elif A<B:
		print("Beto")