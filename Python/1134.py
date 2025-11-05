#1134 - Tipo de Combustível

a=0
alcool = 0
gasolina = 0
diesel = 0
while a>=0:
	a = int(input())
	if a == 1:
		alcool = alcool+1
	elif a ==2:
		gasolina = gasolina+1
	elif a ==3:
		diesel = diesel+1
	elif a ==4:
		print ("MUITO OBRIGADO")
		print ("Alcool: %d"%alcool)
		print ("Gasolina: %d"%gasolina)
		print ("Diesel: %d"%diesel)
		break