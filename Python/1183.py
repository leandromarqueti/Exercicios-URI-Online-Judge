#1183 - Acima da Diagonal Principal

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
qtde = (144 - 12) / 2
#Elementos  no  triângulo  superior
for i in range (0 ,12):
#Soma  elementos  no  triângulo  superior
    for j in range(i+1 ,12):
        soma += mat[i][j]
if o == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma / qtde))