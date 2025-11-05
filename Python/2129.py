#2129 - Fatorial

# -*- coding: utf-8 -*-
vet = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

def ultimonum0Digit(n):
    if n<10:
       return vet[n]
    if (n//10%10)%2 == 0:
        n1 = n%10
        ndiv5 = n//5
        return (6*ultimonum0Digit(ndiv5)*vet[n1])%10
    else:
        n1 = n%10
        ndiv5 = n//5
        return (4*ultimonum0Digit(ndiv5)*vet[n1])%10
i = 1
while True:
    try:
        n = int(input())
        print ("Instancia %d"%i)
        i +=1

        print("%d\n"%ultimonum0Digit(n))


    except EOFError:
        break