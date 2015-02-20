import os 
import time 
cont = 0
x1   = 0
animacion = ['.','..','...']
while x1 < 999:
	x1 = input("Semilla\n>:")

#PRUEBA CON 5735
print "Comenzando semilla = Xi %i\n"%x1
res = x1 ** 2
while res > 0:
	cont += 1 
	if res < 9999999 :
		print "X%i= ^ 2 = 0%i\n"%(cont,res)
		tmp ="0"+str(res)[2:7]
		print "4 No's del Centro 0%s ri = 0.%s"%(str(res)[2:5],tmp[:4])
		print tmp
		res = float(tmp[:4])**2
		print "-------------2"
		time.sleep(2)
	else:
		print "X%i= ^ 2 = %i \n"%(cont,res)
		print "4 No's del Centro %s ri = 0.%s"%(str(res)[2:6],str(res)[2:6])
		res = float(str(res)[2:6])**2
		print "-------------1"
		time.sleep(2)
