import math 
conjunto = []

x   = int(raw_input("ingresa X \n >:"))
a   = int(raw_input("ingresa A \n >:"))
m   = int(raw_input("ingresa M \n >:"))
c   = int(raw_input("ingresa C \n >:"))
res = 0
cont = 1
res  = ((a * x + c)% m)
while x != res:
	conjunto.append(res/float(m))
	print " ( "+str(a)+" ( "+str(res)+" ) + "+str(c)+" ) % " +str(m)
	cont += 1
	res = ((a * res + c)% m)
	print "\t\tRESIDUO>:"+str(res)+" ri "+str(cont)+">:"+str(float(res/float(m)))
	
	
print "total = "+str(cont)


n        = len(conjunto)
m        = int(math.sqrt(float(n)))
Ei       = float(n)/m
Oi       = []
total    = 0
subInt   = 1.0/m
lista_sub= []
#SALTO = ENTERO REDONDEADO
salto = int(subInt*100)
for pos,i in enumerate(xrange(0,110,salto)):
	if i == 99:
		i == 100
	if i == 0:
		pass
	else:
		print "%i) %f"%(pos,i*0.01)
	lista_sub.append(float(i*0.01))


for j in xrange(len(lista_sub)-1):
	cont = 0
	for x in xrange(len(conjunto)):
		if conjunto[x]>=lista_sub[j] and  conjunto[x]<lista_sub[j+1]:
			print "conjunto parte de %f"%lista_sub[j]
			cont +=1



	print cont  
	Oi.append(cont)
print Oi
cant = 0
print "SUB INTERVALOS\tOI\tEi\t(Ei-Oi)^2/Ei"
for l in lista_sub:
	if l == 0.00:
		pass
	else:
		print "%.2f\t\t%i\t%.2f\t     %.2f"%(l,Oi[cant],Ei,((Ei-Oi[cant])**2)/Ei)
		total+=(((Ei-Oi[cant])**2)/Ei)
		cant +=1

print "EL TOTAL FUE"+str(total)
			
		
