#1182 - Coluna na Matriz

c = int(input ())
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
for i in range (0 ,12):
#Soma  elementos  na  coluna c
    soma += mat[i][c]
if o == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma / 12))