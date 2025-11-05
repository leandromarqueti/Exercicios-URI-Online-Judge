#1113 - Crescente e Decrescente

a, b = input().split()
a = int(a)
b = int(b)
c = 0
while c == 0:
	if a>b:
		print("Decrescente")
	elif a<b:
		print("Crescente")
	a, b = input().split()
	a = int(a)
	b = int(b)
	if a==b:
		c= c+1