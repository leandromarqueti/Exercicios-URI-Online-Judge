#1051 - Imposto de Renda

a= float(input())

if a<=2000:
	print("Isento")

elif a>2000 and a<=3000:
	a= a-2000.00
	imposto = a*0.08
	print("R$ %.2f"%imposto)

elif a>3000 and a<=4500:
	a= a-2000.00
	imposto1 = 1000*0.08
	a = a-1000.00
	imposto2 = a*0.18
	imposto = imposto1+imposto2
	print("R$ %.2f"%imposto)

elif a>4500:
	imposto1 = 1000*0.08
	imposto2 = 1499.99*0.18
	a = a-4500.00
	imposto3 = a*0.28
	imposto = imposto1+imposto2+imposto3
	print("R$ %.2f"%imposto)
