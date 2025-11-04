#1652 - Deli Deli

a, b = input().split()
a = int(a)
b = int(b)
 
for i in range (0, a):
	strA, strB = input().split()
	strA = str(strA)
	strB = str(strB)
for i in range (0, b):
	string = str(input())
	if string == "rice" :
		print ("rice")
	elif string == "lobster":
		print("lobsters")
	elif string == "spaghetti":
		print("spaghetti")
	elif string == "strawberry":
		print("strawberries")
	elif string == "octopus":
		print("octopi")
	elif string == "peach":
		print("peaches")
	elif string == "turkey":
		print("turkeys")
	else:
		string.lower()
		if  string[-2::] == "by" or string[-2::] == "cy" or string[-2::] == "dy" or string[-2::] == "fy" or string[-2::] == "gy" or string[-2::] == "hy" or string[-2::] == "jy" or string[-2::] == "ky" or string[-2::] == "ly" or string[-2::] == "my" or string[-2::] == "ny" or string[-2::] == "py" or string[-2::] == "qy" or string[-2::] == "ry" or string[-2::] == "sy" or string[-2::] == "ty" or string[-2::] == "vy" or string[-2::] == "wy" or string[-2::] == "xy" or string[-2::] == "zy":

			string = string[:-1]
			string = string + "ies"
			print(string)
		elif string[-1::] == "o" or string[-1::] == "s" or string[-1::] == "x" or string[-2::] == "ch" or string[-2::] == "sh":
			string = string + "es"
			print(string)
		else:
			print(string+"s")