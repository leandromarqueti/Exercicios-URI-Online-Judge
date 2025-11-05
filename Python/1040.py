#1040 - Média 3

# -*- coding: utf -8 -*-

n1, n2, n3, n4 = input().split()
n1 = float (n1)
n2 = float (n2)
n3 = float (n3)
n4 = float (n4)
media = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10

print("Media: %.1f" % (media))

if media >= 7.0:
	print("Aluno aprovado.")
elif media < 5.0:
	print("Aluno reprovado.")
elif media >= 5.0 and media <7.0:
	print ("Aluno em exame.")
	exame = float (input())
	print ("Nota do exame: %.1f" % (exame))
	media = (media+exame)/2
	if media >= 5.0:
		print ("Aluno aprovado.")
		print ("Media final: %.1f"% (media))
	else:
		print ("Aluno reprovado.")
		print ("Media final: %.1f"% (media))