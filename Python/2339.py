#2339 - Aviões de Papel

# -*- coding: utf -8 -*-

candidatos, papel, folha = input().split()
candidatos = float(candidatos)
papel = float(papel)
folha = float(folha)

if (candidatos * folha) <= papel:
	print ("S")
else:
	print ("N")