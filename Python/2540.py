#2540 - Impeachment do Líder

# -*- coding : utf -8 -*-
while True :
    try :
        n = int ( input ())
        v = input (). split ()
        qtde1 = 0;
        for i in range (0 , n ):
            if v[ i] == '1':
                qtde1 += 1
        if qtde1 >= n * 2 / 3:
            print ("impeachment")
        else :
            print ("acusacao arquivada")
    except EOFError : # Permite capturar erro
        break