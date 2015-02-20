print "ingresa tus 2 semillas"
x1  = input("1>:")
x2  = input("2>:")
x   = input("numero de repeticiones")
arr = []
while len(arr)<x:
	x3 = x2 * x1 
	print "x1 * x2 =%i"%x3
	print "ri = 0.%s"%str(x3)[2:6]
	x1 = x2
	x3 = float(str(x3)[2:6])#conversion antes de pasar
	x2 = x3
	arr.append(x3)


		