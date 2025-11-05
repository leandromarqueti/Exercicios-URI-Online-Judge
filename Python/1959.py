#1959 - Polígonos Regulares Simples

def entrada():
    n,l = map(int,input().split())
    return n,l

def perimetro(n,lado):
    return n*lado

def main():
    n,l=entrada()
    print(perimetro(n,l))

main()