#1043 - Triângulo

# -*- coding: utf -8 -*-

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
perimetro = 0.0
area = 0.0
BmenosC = 0.0
BmaisC = 0.0
AmenosC = 0.0
AmaisC = 0.0
AmenosB = 0.0
AmaisB = 0.0

BmenosC = B-C
BmaisC = B+C
AmenosC = A-C
AmaisC = A+C
AmenosB = A-B
AmaisB = A+B
if A > BmenosC and A < BmaisC and B > AmenosC and B < AmaisC and C > AmenosB and C < AmaisB:
	perimetro = A+B+C
	print ("Perimetro = %.1f" % perimetro)
else:
	area = ((A+B)*C)/2
	print ("Area = %.1f" % area)