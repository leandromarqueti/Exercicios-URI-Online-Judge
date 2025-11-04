#1187 - Área Superior

soma_ou_media = input()
matriz = []

for i in range(12):
    for j in range(12):
        valor = float(input())
        if (i < 5) and (j <= 10-i) and (j > i):
            matriz.append(valor)

if soma_ou_media == "S":
    print(("%.1f")%(sum(matriz)))
else:
    print(("%.1f")%(sum(matriz)/len(matriz)))