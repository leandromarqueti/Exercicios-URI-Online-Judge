#2375 - Sedex

D = int(input())
A, L, P = input().split()
A = int(A)
L = int(L)
P = int (P)

if D>=1 and D<=10000 and A>=1 and A<=10000 and L>=1 and L<=10000 and P>=1 and P<=10000:
	if D<=A and D<=L and D<=P:
		print("S")
	else:
		print("N")