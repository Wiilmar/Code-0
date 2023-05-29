print('Calculadora')
a = int(input('Ingrese un numero: '))
print('[1] Multiplicacion [2] Sumar [3]Resta [4] Division')
operador = int(input('Ingrese alguno de los siguientes operadores con base al numero: '))
b = int(input('Ingrese otro numero: '))
if operador == 1:
    operador = (a*b)
    print('el resultado de la multiplicacion', a,'*',b, 'es:', operador)
elif operador == 2:
    operador = (a+b)
    print('el resultado de la suma', a,'+',b, 'es:', operador)
elif operador == 3:
    operador = (a-b)
    print('el resultado de la resta', a,'-',b, 'es:', operador)
elif operador == 4:
    operador = (a/b)
    print('el resultado de la division', a,'/',b, 'es:', operador)
else:
    print('Usted ingreso un operador diferente')
print('Fin de la calculadora')

