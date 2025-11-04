#2392 - Pulo do Sapo

resultado=[ ]*100

for i in range(0,100):
		
	resultado.insert(i, 0)
		
Pedras, Sapos = input().split()
Pedras = int(Pedras)
Sapos = int(Sapos)

for i in range (0, Sapos):
	Posicao, Distancia = input().split()
	Posicao=int(Posicao)
	Distancia=int(Distancia)
	Posicao-=1

	j= Posicao
	while j < Pedras:
		resultado.insert(j, 1)
		j+= Distancia
			
	j= Posicao
	while j>=0:
		resultado.insert(j, 1)
		j-= Distancia
for i in range (0, Pedras):
	print (resultado[i])