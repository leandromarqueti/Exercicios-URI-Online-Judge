#1807 - Triângulo Trinomial, a Vingança

r = int(input())
# r = (3**r)%2147483647
# r = power(3, r)%2147483647
r = pow(3, r, 2147483647)
print(r)