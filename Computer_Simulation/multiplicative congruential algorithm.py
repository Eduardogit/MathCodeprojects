import math
import os
#DECLARACION VARIABLES
ini      = [
			"\t\t+--------------------+\n"
			"\t\t|  A l g o r i t m o |\n"
			"\t\t|    multiplicativo  |\n"
			"\t\t|     Chi Cuadrada   |\n"
			"\t\t|           Y        |\n"
			"\t\t| Prueba de Corridas |\n"
			"\t\t+--------------------+\n"
			] 
#---VARIABLES DE GENERACION
sustitution = 1
conjunto    = []
res         = 0
cont        = 0
ri          = 0
#---VARIABLES DE INTERVALOS
n        = 0
m    	 = 0
ei 		 = 0
oi 		 = 0
total 	 = 0
subint	 = 0
lista_sub= []
#INPUT OF VARIABLES
for presentation in ini:
	print presentation 
while sustitution == 1:
	if cont  == 0:
		print "[+]Formula\n\t(A * Xi)mod M"
		a     = input("\t\nA>:")
	elif cont == 1:
		os.system('clear')
		print "[+]Formula\n\t(%i * Xi)mod M"%(a)
		x     = input("\tingresa X \n >:")
	elif cont == 2:
		os.system('clear')
		print "[+]Formula\n\t(%i * %i)mod m"%(a,x)
		m     = input("\tingresa M \n >:")
	elif cont == 3:
		os.system('clear')
		print "[+]Formula\n\t(%i * %i)mod %i"%(a,x,m)
		print "[!]The formula is correct ?\n\t[1] YES\n\t[2] NO"
		if input() == 1:
			sustitution = 2
		else:
			sustitution = 1
			cont =-1
			a    = 0
			x    = 0
			m    = 0
	cont +=1
#---END INPUT OF VARIABLES----#

#GENERATING  VARIABLES
cont = 0
while x != res:
	if cont == 0:
		print "[+](%i ( %i) )  %i"%(a,x,m)
		res = ((a * x)% m)
		ri  = float(res)/float(m)
		conjunto.append(ri)
		print "[+]Residuo = %i ri = %f"%(res,ri)
	else:
		print "[+](%i ( %i) )  %i"%(a,res,m)
		res = ((a * res )% m)
		ri = float(res)/float(m)
		conjunto.append(ri)
		print "[+]Residuo = %i ri = %f"%(res,ri)
	cont +=1
#---END OF VARIABLES GENERATING ---#
print "[+]Iterations  [%i] \n"%cont
print "[+] Array ri \n%s\n\n"%conjunto


#conjunto = [0.397,0.993,0.674,0.426,0.46,0.189,0.112,0.37,0.909,0.172
#		   ,0.832,0.371,0.688,0.054,0.224,0.753,0.191,0.314,0.764,0.516
#		   ,0.966,0.729,0.055,0.022,0.99,0.73,0.589,0.731,0.999,0.439
#		   ,0.472,0.067,0.499,0.742,0.786,0.797,0.347,0.742,0.303,0.393
#		   ,0.797,0.189,0.494,0.674,0.393,0.292,0.426,0.213,0.718,0.268
#		   ,0.101,0.977,0.235,0.898,0.461,0.876,0.057,0.472,0.933,0.123
#		   ,0.696,0.843,0.178,0.641,0.011,0.707,0.819,0.641,0.056,0.945
#		   ,0.966,0.562,0.775,0.674,0.977,0.562,0.303,0.944,0.415,0.527
#		   ,0.404,0.549,0.792,0.84,0.246,0.562,0.404,0.281,0.819,0.459
#		   ,0.603,0.992,0.252,0.19,0.881,0.84,0.64,0.663,0.444,0.652]


n 	  	  = len(conjunto)
m 	  	  = int(math.sqrt(float(n)))
ei    	  = float(n)/m
oi    	  = []
subint	  = 1.0/m
salto     = int(subint*100)
total 	  = 0
lista_sub = []

#GENERATING INTERVAL RANGE 
for pos,i in enumerate(xrange(0, 100+salto, salto)):
	print "%i) %f"%(pos+1,i*0.01)
	lista_sub.append(float(i*0.01))
#GENERATING OBSERVED RUNNING
print lista_sub
for j in xrange(len(lista_sub)-1):
	cont = 0
	for x in xrange(len(conjunto)):
		if conjunto[x]>=lista_sub[j] and  conjunto[x]<lista_sub[j+1]:
			print "conjunto parte de %f"%lista_sub[j]
			cont +=1
	print cont 
	oi.append(cont)
print oi
porcent = input("CUAL ES EL VALOR DE TOLERANCIA EN PORCENTAJE\n>:")
porcent = 100 - porcent 
porcent = porcent * 0.010
print porcent
#GENERATING CHI TABLE
print "SUB INTERVALOS\tOI\tEi\t(Ei-Oi)^2/Ei"
for l in xrange(len(lista_sub)-1):
	print "%.2f- %.2f\t%i\t%.2f\t     %.2f"%(lista_sub[l],lista_sub[l+1],oi[l],ei,((ei-oi[l])**2)/ei)
	total+=(((ei-oi[l])**2)/ei)

print "EL TOTAL FUE"+str(total)
print "INGRESA VALOR DE LA TABLA CON ESTOS DATOS \n (%.2f , %i)\n\n"%(porcent,m-1)
result = float(input(">:"))
if result < total:
	print "(%.2f > %.2f)"%(total,result)
	print "Se RECHAZA que el conjunto de numeros \nri tiene una distribucion uniforme"

else:
	print "(%.2f < %.2f)"%(total,result)
	print "Se ACEPTA que el conjunto de numeros \nri tiene una distribucion uniforme"


print "###########REALIZANDO PRUEBA DE CORRIDAS#############"
n      = len(conjunto)
m      =int(math.sqrt(len(conjunto)))
n0     = 0
n1     = 0
co     = 0
matriz = []
for i in conjunto:
	if i > 0.5:
		matriz.append(1)		
		n0+=1
	else:
		matriz.append(0)
		n1+=1
for j in xrange(len(matriz)-1):
	if matriz[j] == matriz[j+1]:
		pass
	else:
		co+=1
print matriz
mco = ((2*(n0*n1))/n)+(0.5)
oco = (2*(n0*n1)*(2*(n0*n1)-n))/(n**2)*n-1
zo = (co - mco )/ math.sqrt(oco)
print "\nCorridas observadas %i\n"%(co+1.0)
print "Valor esperado \nMco     = %f"%mco
print "Varianza \nO^2 Co  = %f "%oco
print "Estadistico\nZo= %f"%zo