#1146 - Sequências Crescentes

while 1:
	a= int(input())
	if a==0:
		break
	soma = "1"
	for i in range (2,a+1):
		soma=soma+ " "+ str(i)

	print ("%s"%soma)