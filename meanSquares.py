res =input(">:")
gen =input("N a generar>:")
res = res ** 2
cont = 0
arr = []
while len(arr) < gen:
	cont += 1
	if res < 99999 :
		tmp = "0"+str(res)
		print tmp
		res = float(str(tmp)[1:4])**2
		print res
		arr.append(res)
		print "-------4"
	elif res < 999999 :
		res = float(str(res)[1:5])**2
		print res 
		arr.append(res)
		print "-------3"

	elif res < 9999999:
		tmp ="0"+str(res)
		print tmp  
		res = float(tmp[2:6])**2
		print res
		arr.append(res)
		print "-------2"
	else:
		res = float(str(res)[2:6])**2
		print res
		arr.append(res)
		print "-------1"
print cont