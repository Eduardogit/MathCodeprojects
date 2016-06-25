#---- INGRESO DE DATOS--+
puts  "Teclea a A "     #
a   = gets.to_i         # 5
puts  "Teclea a X "     #
x   = gets.to_i         # 4
puts  "Teclea a C "     #
c   = gets.to_i         # 7
puts  "Teclea a M "     #
m   = gets.to_i         # 8
#---- INGRESO DE DATOS--+

#-----GENERANDO VARIABLES --------------------------------------------------------
ri  = []							   
res = 0								   
cont= 0							       
while x!=res #                <----- hasta que x (que ingresamos) sea igual a res                 
#-------PRIMERA OPERACION--------------+
	if cont == 0                     # |este bloque hace esta operacion
		res = ((a * x + c)% m)       # | <----- a * x +c
		ri.push(res.to_f/m.to_f)     # | 
		puts "#{res}  >:#{ri[cont]}" # |
		cont+=1                      # |
	end                              # |
#--------------------------------------+
#----------------- OPERACION CON res -------------+
	res = ((a * res + c)% m)                    # |<----- a * res + c
	ri.push(res.to_f/m.to_f)                    # |este bloque hace esta operacion
	puts "#{res}  >:#{ri[cont]}"                # |
	cont+=1                                     # |
#-------------------------------------------------+
end
puts "se alcanzaron #{cont} Xi" #CONTEO DE LAS REPETICIONES
#-------FIN DE GENERACION DE VARIABLES ---------------------------------------------

#---------COMIENZA CHI ------------------------------------------------------------
puts "\n\n\n \tPRUEBA DE CHI CUADRADA \n\n\n"
n = cont.to_f   # => n igual al  total de las variables
m = Math.sqrt(n)# => m igual a raiz cuadrada de n
e = n/m         # => e(Ei) igual a la division de n /m 
o =[]           # => o(Oi) Arreglo que contara los numeros dentro del intervalo
es =0           
inter = 1.0/m
contador = 0
intervalo = []   
0.step(1,inter){|i| intervalo.push(i)}  # =>  SE GENERA EL RANGO DE 0 A 1
puts "ri #{ri}" 					    #se imprime el rango que quedo

#--------------------------ACOMODANDO VARIABLES EN SU INTERVALOR--------
for i in 0...intervalo.length       #de 0 hasta el tamaño del arreglo 
	contador = 0					#lleva el conteo de los intervalos de los datos
	for j in ri                     #otro for que compara los datos decimales con los intervalos
#---------------COMPARA SI LLEGO AL FINAL DEL ARREGLO---------------------------------+
		if intervalo[i] == intervalo.last                                            #|
			if  j >= intervalo.last                                                  #| <-- numeros decimales que entran en el ultimo           
				contador+=1                                                          #|       intervalo
			end                                                                      #|
#-------------------------------------------------------------------------------------+
		elsif j >= intervalo[i] and j <= intervalo[i+1]#------------------------------+
			contador+=1 #                             COMPARAMOS LOS DEMAS INTERVALOS |
		end             #                             EXCEPTO EL ULTIMO QUE SE COMPARA|
	end                 #                             EN EL BLOQUE DE ARRIBA          |
		o.push(contador)#                         <-- se le agrega el conteo de cada intervalo
end                     #                                                             |
#-------------------------------------------------------------------------------------+
suma = 0
puts "intervalo\t OI\t EI\t\t (EI-OI)/EI"
for i in 0...intervalo.length
	es = ((e.to_f-o[i].to_f)**2)/es
	suma +=es
	puts "#{(intervalo[i]*100).to_i.to_f/100}\t\t #{o[i]}\t #{e} #{es}"#<--- TODO ESTO IMPRIME LA TABLA
end
puts "\nsuma es #{suma}"


#--------CORRIDAS ----------------------

n      = ri.length
m      = Math.sqrt(ri.length).floor
n0     = 0
n1     = 0
co     = 0
arreglo_cerosyunos = []
for i in ri
	if i > 0.5
		arreglo_cerosyunos.push(1)		
		n0+=1
	else
		arreglo_cerosyunos.push(0)
		n1+=1
	end
end
cont = 0
for j in arreglo_cerosyunos
	if j == arreglo_cerosyunos[cont+1]
	else
		co+=1
	end
	cont += 1
end
puts "\n\n\n\tPRUEBA DE CORRIDAS \n\n\n\n"
print "\t#{arreglo_cerosyunos}"
M = ((2*(n0*n1))/n)+(0.5)
C = (2*(n0*n1)*(2*(n0*n1)-n))/(n**2)*n-1
Z = (co - M )/ Math.sqrt(C)
puts "\n\nCorridas #{co}\n"
puts "\nM * co     = #{M}"
puts "\nO^2 * Co  = #{C} "
puts "\nZ = #{Z}"























w