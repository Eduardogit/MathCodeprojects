import math
print "ingresa tus 2 semillas"
x1  = input("1>:")
x2  = input("2>:")
x   = input("numero de repeticiones")
arreglo = []
while len(arreglo)<x:
	x3 = x2 * x1 
	print "x1 * x2 =%i"%x3
	print "ri = 0.%s"%str(x3)[2:6]
	x1 = x2
	x3 = float(str(x3)[2:6])
	x2 = x3
	arreglo.append(x3*.0001)

print arreglo

n      = len(arreglo)
m      =int(math.sqrt(len(arreglo)))
n0     = 0
n1     = 0
corridas     = 0
ceros = []
for i in arreglo:
	if i > 0.5:
		ceros.append(1)		
		n0+=1
	else:
		ceros.append(0)
		n1+=1
for j in xrange(len(ceros)-1):
	if ceros[j] == ceros[j+1]:
		pass
	else:
		corridas+=1
print "\nCORRIDAS %i\n"%(corridas+1.0)
print ceros
XMCO = ((2*(n0*n1))/n)+(0.5)
print "Valor 1 \n mco     = %f"%XMCO
XCO = (2*(n0*n1)*(2*(n0*n1)-n))/(n**2)*n-1
print "Valor 2 \nO^2 Co  = %f "%XCO
z = (corridas - XMCO )/ math.sqrt(XCO)
print "Valor 3\nZ= %f"%z

por = input("INGRESA TU PORCENTAJE ")
print ""+str(por)+","+str(m-1)
tabla =  input("VALOR DE LA TABLA")
if tabla > z :
	print "Se acepta que el conjunto de numeros es INDEPENDIENTE"
else:
	print "Se Rechaza que el conjunto de numeros es INDEPENDIENTE"
