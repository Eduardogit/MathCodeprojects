from time import sleep
message   = []
polinomio = []
resultado = []
arr = []
	# pol = > 4,2,0
	# mens= > [0, 4, 5, [5, 4], 6, [6, 4], [6, 5], [6, 5, 4]]

def div(pol,m):
	rx = []
	if type(m) == list:
		resta = valMax(m) - valMax(pol)
	else:
		resta = m - valMax(pol)
	for i in pol:
		rx.append(i + resta)
		print "i = %i resta = %i"%(i,resta)
	comp = comparacion(rx , m)
	print comp , pol
	if valMax(comp) == valMax(pol):
		rx = []
		resta = valMax(comp) - valMax(pol)
		for i in pol:
			rx.append(i + resta)
		comp = comparacion(rx,comp)
	elif valMax(comp) >= valMax(pol):
		div(pol,comp)
	return converBin(m,comp)





def comparacion(r,msj1):
	resComp = []
	if type(r) == list and type(msj1) == list:
		for i in r:
			if i not in msj1:
				resComp.append(i)
	else:
		for i in r:
			if i == msj1:
				pass
			elif i != msj1:
				print i
				resComp.append(i)
	return resComp





def converBin(arr,msj):
	print arr
	print msj
	if type(arr)== list:
		for x in arr:
			msj.append(x)
	elif type(arr) == int:
		msj.append(arr)

	msj.sort()
	msj.reverse()
	print msj
	bina = [0,0,0,0,0,0,0]
	for x in xrange(0, 7):
		if x in msj:
			bina[x] = 1
	bina.reverse()
	msj = bina
	print msj
	return msj
		


def msj(x):
	dx = []
	for i in xrange(0, 8):
		if 	 i == 0:
			dx.append(0)
		elif i == 1:
			dx.append(x * 1)
		elif i == 2:
			dx.append(x+1)
		elif i == 3:
			dx.append([x+1,x])
		elif i == 4:
			dx.append(x+2)
		elif i == 5:
			dx.append([x+2,x])
		elif i == 6:
			dx.append([x+2,x+1])
		elif i == 7:
			dx.append([x+2,x+1,x])
	return dx

def valMax(x):
	res = 0
	for i in x:
		res = (res , i)[i>res]
	return res

#------------------INICIO DEL PROGRAMA---------------------#
valores = ['x4','x2','1']
print "Polinomio G(x) => %s"%valores
#------------------PURGANDO LAS 'X' DEL POLINOMIO----------#
for i in valores:
	if i == 'x':
		i = '1'
	elif i == '1':
		i = '0'
	polinomio.append(int(i[-1]))
#----------IMPRIMIENTO POLINOMIO PURGADO Y VALOR MAX-------#
print "POLINOMIO => %s"%polinomio
valm    = valMax(polinomio)
print "VALOR MAX => %s"%valm
message = msj(valm) #VALORES DE MENSAJES EN ARRAY
#------------------REALIZANDO DIVISION --------------------#

print "MENSAJE  =>   %s"%message

for i in message:
	if i == 0:
		pass
	else:
		print "	Mensaje   "+str(i)+" Polinomio   "+str(polinomio)
		resultado.append(div(polinomio,i))

for i in resultado:
	print i





















