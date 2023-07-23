# Para comentar en linea debo usar la tecla '#'

# Esto es una suma expresiva
sum = 1 + 2
print('La suma de 1 + 2 es:', sum, '(expresiva)')

#Esto es una suma declarativa
Num1 = 2
Num2 = 2
Resultado = (Num1 + Num2)
#El comando print me sirve para imprimir en pantalla
print('La suma de', Num1, '+', Num2, 'es', Resultado, '(declarativa)')

Cadena = 'Esto es una cadena'
Entero = 1 #Esto es Int
Float = 1.2 #Esto es un float
Boleano = True #Esto es un Boleanoo
print(Boleano)

#operadores de signo
valor = 2
#Al usar el operador '+=' la variable 'valor' incrementara en 2.
valor += 2
#Al usar el operador '-=' la variable 'valor' se reduce en 2.
valor -= 2
#Al usar el operador '*=' la variable 'valor' se multiplica por 5.
valor *= 5
print(valor)

#conversion de tipo de datos
numero = 32254492
nombre1 = 'Wilman'
# Debo convertir ciertas variables a string para poder usar el siguiente comando:
#print('Hola' + nombre1 + 'Tu numero es:' + numero)
print('Hola ' + nombre1 + ' Tu numero es: ' + str(numero))

#Para saber el tipo de dato de una variable
print(type(numero))

numerocientifico = 430000000000000.67
print(numerocientifico)

name = 'wilman'
lastname = "rodriguez"
#1 Forma de imprimir
template = 'Hola, mi nombre es {} y mi apellido es {}'.format(name,lastname)
print (template)

#2 forma de imprimir
template = 'Que tal, mi nombre es ' + name + ' y mi apellido es ' + lastname
print(template)

#3 forma de imprimir mas optima
# La 'f' significa format, me permite que las llaves funcionen 
template = f"Quibo, mi nombre es {name} y mi apellido es {lastname}"
print(template)

template= name + ' '+ lastname
print(template)

boleano = True
print(type(boleano))

#Se triplica el hola
print('Hola' * 3)

#Invertir boleanos
print(not True)
print(not False)