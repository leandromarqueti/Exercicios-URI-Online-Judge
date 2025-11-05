#1318 - Bilhetes Falsos

# -*- coding: utf-8 -*-
while True:
  originais,pessoas = [int(x) for x in input().split()]
  if originais == 0 and pessoas == 0:
    break
  bilhetes = input().split() 
  lista = set(bilhetes) 
  falsos = 0
  for e in lista:
    x = bilhetes.count(e)
    if x > 1:
      falsos +=1
  print(falsos)
  