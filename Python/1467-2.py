#1467 - Zerinho ou Um

vencedor = 'h'
while vencedor != 'A' or vencedor != 'B' or vencedor != 'C':
	a, b, c = input().split()
	a = int(a)
	b = int(b)
	c = int(c)
	if a==b and a==c and b==c:
		vencedor = '*'
		print ("*")
	elif a!=b and b==c:
		vencedor = 'A'
		print ("A")
	elif a==c and b!=a:
		vencedor = 'B'
		print ("B")
	else:
		vencedor = 'C'
		print ("C")