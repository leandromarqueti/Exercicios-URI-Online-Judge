#2473 - Loteria

# -*- coding: utf-8 -*-
a = input().split()
b = input().split()
c=0

if a[0] == b[0]:
	c+=1
if a[0] == b[1]:
	c+=1
if a[0] == b[2]:
	c+=1
if a[0] == b[3]:
	c+=1
if a[0] == b[4]:
	c+=1
if a[0] == b[5]:
	c+=1

if a[1] == b[0]:
	c+=1
if a[1] == b[1]:
	c+=1
if a[1] == b[2]:
	c+=1
if a[1] == b[3]:
	c+=1
if a[1] == b[4]:
	c+=1
if a[1] == b[5]:
	c+=1

if a[2] == b[0]:
	c+=1
if a[2] == b[1]:
	c+=1
if a[2] == b[2]:
	c+=1
if a[2] == b[3]:
	c+=1
if a[2] == b[4]:
	c+=1
if a[2] == b[5]:
	c+=1

if a[3] == b[0]:
	c+=1
if a[3] == b[1]:
	c+=1
if a[3] == b[2]:
	c+=1
if a[3] == b[3]:
	c+=1
if a[3] == b[4]:
	c+=1
if a[3] == b[5]:
	c+=1

if a[4] == b[0]:
	c+=1
if a[4] == b[1]:
	c+=1
if a[4] == b[2]:
	c+=1
if a[4] == b[3]:
	c+=1
if a[4] == b[4]:
	c+=1
if a[4] == b[5]:
	c+=1

if a[5] == b[0]:
	c+=1
if a[5] == b[1]:
	c+=1
if a[5] == b[2]:
	c+=1
if a[5] == b[3]:
	c+=1
if a[5] == b[4]:
	c+=1
if a[5] == b[5]:
	c+=1

if c == 3:
	print ("terno")
elif c == 4:
	print ("quadra")
elif c == 5:
	print ("quina")
elif c == 6:
	print ("sena")
elif c<3:
	print ("azar")