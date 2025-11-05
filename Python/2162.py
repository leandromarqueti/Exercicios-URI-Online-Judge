#2162 - Picos e Vales

# -*- coding : utf -8 -*-
n = int ( input ())
hs = input (). split ()
for i in range (0 , n ):
    hs [i] = int ( hs [i ])
    
padrao = 1
# Procura vale seguido de um vale ou pico seguido de pico
forma = 0 #1 = Vale , 2 = Pico

for i in range (1 , n ):
    if hs [i] < hs [i -1]:
        if forma == 1: #Se vale
            padrao = 0
            break
        else :
            forma = 1
    elif hs [i] > hs [i -1]:
        if forma == 2: #Se pico
            padrao = 0
            break
        else :
            forma = 2
    else :
        padrao = 0
        break
print ( padrao )