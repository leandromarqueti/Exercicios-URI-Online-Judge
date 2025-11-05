#1150 - Ultrapassando Z

x = int(input())
z = int(input())
lista = []
while(z <= x):
  z = int(input())
for i in range(x, z):
  lista.append(i)
  if(sum(lista) > z):
    print(len(lista))
    break