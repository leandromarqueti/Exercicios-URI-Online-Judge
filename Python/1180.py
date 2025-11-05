#1180 - Menor e Posição

n=int(input())
x=[]
a=list(map(int,input().split()))
for i in range (0, n):
    x.insert(i,a[i])
print("Menor valor: %d" %(min(x)))
for i in range(0, n):
    if x[i]==min(x):
        pos=i
print("Posicao: %d" %pos)