#1189 - Área Esquerda

o = input()
mat = [None] * 12
#Cria  uma  matriz  12x12
for i in range(0, 12):
    mat[i] = [None] * 12
for i in range (0 ,12):
#Lê os 144  elementos
    for j in range (0 ,12):
        mat[i][j] = float(input ())
soma = 0;
qtde = (144 - 24) / 4
#Elementos  no  triângulo  superior
for i in range (0,6):
#Soma no  triângulo  esquerdo (cima)
    for j in range(0,i):
#Aumento  colunas
        soma += mat[i][j]
for i in range (6 ,12):
#Soma no  triângulo  esquerdo (baixo)
    for j in range(0,12-i-1):
#Reduzo  colunas
        soma += mat[i][j]
if o == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma / qtde))