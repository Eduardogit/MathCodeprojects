print "Teclea a A "
a   = gets.to_i
print "Teclea a X "
x   = gets.to_i
print "Teclea a C "
c   = gets.to_i
print "Teclea a M "
m   = gets.to_i
#----TERMINA INGRESO DE DATOS---
ri  = []
res = 0
cont= 0
#-----GENERANDO VARIABLES RI 
while x!=res
	if cont == 0
		res = ((a * x + c)% m)
		ri.push(res.to_f/m.to_f)
		puts "#{res}  >:#{ri[cont]}"
		cont+=1
	end
	res = ((a * res + c)% m)
	ri.push(res.to_f/m.to_f) #<<
	puts "#{res}  >:#{ri[cont]}"
	cont+=1
end

puts "se alcanzaron #{cont} Xi"
#---------COMIENZA CHI ---------
n = ri.length
n = n.to_f
m = Math.sqrt(n)
e = n/m
o = []
intervalo = 1.to_f/m
t = 0


#---------COMIENZA CORRIDAS ----
n      = ri.length
m      = Math.sqrt(ri.length).floor
n0     = 0
n1     = 0
co     = 0
matriz = []
for i in ri
	if i > 0.5
		matriz.push(1)		
		n0+=1
	else
		matriz.push(0)
		n1+=1
	end
end
cont = 0
for j in matriz
	if j == matriz[cont+1]
	else
		co+=1
	end
	cont += 1
end
print matriz
mco = ((2*(n0*n1))/n)+(0.5)
oco = (2*(n0*n1)*(2*(n0*n1)-n))/(n**2)*n-1
zo = (co - mco )/ Math.sqrt(oco)
puts "\nCorridas observadas #{co}\n"
puts "Valor esperado \nMco     = #{mco}"
puts "Varianza \nO^2 Co  = #{oco} "
puts "Estadistico\nZo= #{zo}"


