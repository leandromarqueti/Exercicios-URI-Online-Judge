#1221 - Primo Rápido

number = int(input())
for i in range (0, number):
	n = int(input())
	if (n == 2):
		print("Prime")
		continue
	elif (n % 2 == 0):
		print ("Not Prime")
		continue
	primo = True
	for i in range(3,int(n**(1/2)+1),2):
		if (n % i == 0):
			primo = False
			break
	if (primo):
		print ("Prime")
	else:
		print ("Not Prime")