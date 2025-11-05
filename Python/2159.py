#2159 - Número Aproximado de Primos

import math
numero=int(input())
minimo=numero/math.log(numero)
maximo=minimo*1.25506
print ("%.1f"%minimo +" "+ "%.1f"%maximo )