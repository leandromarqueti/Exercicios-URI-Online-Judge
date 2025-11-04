#1120 - Revisão de Contrato

digito, numero = list(map(int, input().split()))
lista = []

for i in range(numero):
  if numero[i] != digito:
    lista.append(numero[i])
print(lista)