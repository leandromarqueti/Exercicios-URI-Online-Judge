#1046 - Tempo de Jogo

a, b = input().split()
a = int (a)
b = int (b)

if a==b:
	print ("O JOGO DUROU 24 HORA(S)")
elif a >= 12:
	if a<b:
		print("O JOGO DUROU %d HORA(S)"%(b-a))
	else:
		c = 24 - a
		print("O JOGO DUROU %d HORA(S)"%(b+c))
else:
	if a<b and b<= 12:
		print("O JOGO DUROU %d HORA(S)"%(b-a))

	elif a < b and b>12:
		c= b-12
		d= 12-a
		print("O JOGO DUROU %d HORA(S)"%(c+d))
	elif a>b:
		c=24-a
		print("O JOGO DUROU %d HORA(S)"%(b+c))