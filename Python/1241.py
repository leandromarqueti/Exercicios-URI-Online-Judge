#1241 - Encaixa ou Não II

qte = int(input())

for i in range(qte):
    A, B = list(map(str,input().split()))
    if A[-len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")