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