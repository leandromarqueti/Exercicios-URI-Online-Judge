#1038 - Lanche

# -*- coding: utf -8 -*-

A, B = input().split()
A = int (A)
B = int (B)

if A == 1:
	A = B*4.00
	print("Total: R$ %.2f" % (A))
elif A == 2:
	A = B*4.50
	print("Total: R$ %.2f" % (A))	
elif A == 3:
	A = B*5.00
	print("Total: R$ %.2f" % (A))
elif A == 4:
	A = B*2.00
	print("Total: R$ %.2f" % (A))
elif A == 5:
	A = B*1.50
	print("Total: R$ %.2f" % (A))