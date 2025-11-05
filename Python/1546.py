#1546 - Feedback

# -*- coding: utf -8 -*-

n = int (input())
for _ in range (0, n):
	k=int(input())
	for _ in range(0, k):
		c=int(input())
		if c == 1:
			print("Rolien")
		elif c == 2:
			print ("Naej")
		elif c == 3:
			print ("Elehcim")
		else:
			print("Odranoel")