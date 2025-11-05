#2376 - Copa do Mundo

# -*- coding: utf-8 -*-
v1 = 'u'
v2 = 'u'
v3 = 'u'
v4 = 'u'
v5 = 'u'
v6 = 'u'
v7 = 'u'
v8 = 'u'
v9 = 'u'
v10 = 'u'
v11 = 'u'
v12 = 'u'
v13 = 'u'
v14 = 'u'
v15 = 'u'

A, B = input().split()
A = int(A)
B = int(B)
while A==B or A<0 and A>20 and B<0 and B>20:
	A, B = input().split()
if A > B:
	v1 = 'A'
elif A < B:

C, D = input().split()
C = int(C)
D = int(D)
while C==D or C<0 and C>20 and D<0 and D>20:
	C, D = input().split()
if C > D:
	v2 = 'C'
elif C < D:
	v2 = 'D'

E, F = input().split()
E = int(E)
F = int(F)
while E==F or E<0 and E>20 and F<0 and F>20:
	E, F = input().split()
if E > F:
	v3 = 'E'
elif E < F:
	v3 = 'F'

G, H = input().split()
G = int(G)
H = int(H)
while G==H or G<0 and G>20 and H<0 and H>20:
	G, H = input().split()
if G > H:
	v4 = 'G'
elif G < H:
	v4 = 'H'

I, J = input().split()
I = int(I)
J = int(J)
while I==J or I<0 and I>20 and J<0 and J>20:
	I, J = input().split()
if I > J:
	v5 = 'I'
elif I < J:
	v5 = 'J'

K, L = input().split()
K = int(K)
L = int(L)
while K==L or K<0 and K>20 and L<0 and L>20:
	K, L = input().split()
if K > L:
	v6 = 'L'
elif K < L:
	v6 = 'L'

M, N = input().split()
M = int(M)
N = int(N)
while M==N or M<0 and M>20 and N<0 and N>20:
	M, N = input().split()
if M > N:
	v7 = 'M'
elif M < N:
	v7 = 'N'

O, P = input().split()
O = int(O)
P = int(P)
while O==P or O<0 and O>20 and P<0 and P>20:
	O, P = input().split()
if O > P:
	v8 = 'O'
elif O < P:
	v8 = 'P'

AB, CD = input().split()
AB = int(AB)
CD = int(CD)
while AB==CD or AB<0 and AB>20 and CD<0 and CD>20:
	AB, CD = input().split()
if AB > CD:
	v9 = v1
elif AB < CD:
	v9 = v2

EF, GH = input().split()
EF = int(EF)
GH = int(GH)
while EF==GH or EF<0 and EF>20 and GH<0 and GH>20:
	EF, GH = input().split()
if EF > GH:
	v10 = v3
elif EF < GH:
	v10 = v4

IJ, KL = input().split()
IJ = int(IJ)
KL = int(KL)
while IJ==KL or IJ<0 and IJ>20 and KL<0 and KL>20:
	IJ, KL = input().split()
if IJ > KL:
	v11 = v5
elif IJ < KL:
	v11 = v6

MN, OP = input().split()
MN = int(MN)
OP = int(OP)
while MN==OP or MN<0 and MN>20 and OP<0 and OP>20:
	MN, OP = input().split()
if MN > OP:
	v12 = v7
elif MN < OP:
	v12 = v8

AD, EH = input().split()
AD = int(AD)
EH = int(EH)
while AD==EH or AD<0 and AD>20 and EH<0 and EH>20:
	AD, EH = input().split()
if AD > EH:
	v13 = v9
elif AD < EH:
	v13 = v10

IL, MP = input().split()
IL = int(IL)
MP = int(MP)
while IL==MP or IL<0 and IL>20 and MP<0 and MP>20:
	IL, MP = input().split()
if IL > MP:
	v14 = v11
elif IL < MP:
	v14 = v12

AH, IP = input().split()
AH = int(AH)
IP = int(IP)
while AH==IP or AH<0 and AH>20 and IP<0 and IP>20:
	AH, IP = input().split()
if AH > IP:
	v15 = v13
elif AH < IP:
	v15 = v14
print ("%s"%v15)