#1796 - Economia Brasileira

# -*- coding: utf-8 -*-
Q = int(input())
V = [int(x) for x in input().split()]
media = Q/2
if sum(V)>=media:
    print("N")
else:
    print("Y")