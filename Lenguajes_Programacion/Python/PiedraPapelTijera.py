# Pieda papel y tijera contra la computadora
# Jugador1 = input('Escoge una opcion [1] Piedra [2] Papel [3] Tijera: ')
# Jugador2 = 'Piedra'

# if Jugador1 == Jugador2 or Jugador1 == 'piedra':
#     print('Empate')
# elif Jugador1 == 'Tijera' or Jugador1 == 'tijera':
#     print('Perdiste')
# elif Jugador1 == 'Papel' or Jugador1 == 'papel':
#     print('Ganaste')
# else:
#     print('Opcion invalida')

#Piedra papel y tijera con dos jugadores
Jugador1 = input('[Jugador 1] Escoge una opcion [1] Piedra [2] Papel [3] Tijera: ')
Jugador2 = input('[Jugador 2] Escoge una opcion [1] Piedra [2] Papel [3] Tijera: ')

if Jugador1 == 'piedra' and Jugador2 == 'tijera':
    print('Jugador Uno gana')
elif Jugador1 == 'piedra' and Jugador2 == 'piedra':
    print('Empate')
elif Jugador1 == 'piedra' and Jugador2 == 'papel':
    print('Jugador 2 Gana')
elif Jugador1 == 'papel' and Jugador2 == 'piedra':
    print('Jugador 1 Gana')
elif Jugador1 == 'papel' and Jugador2 == 'tijera':
    print('Jugador 2 Gana')
elif Jugador1 == 'papel' and Jugador2 == 'papel':
    print('Empate')
elif Jugador1 == 'tijera' and Jugador2 == 'piedra':
    print('Jugador 2 Gana')
elif Jugador1 == 'tijera' and Jugador2 == 'tijera':
    print('Empate')
elif Jugador1 == 'tijera' and Jugador2 == 'papel':
    print('Jugador 1 Gana')
elif Jugador2 == 'piedra' and Jugador1 == 'tijera':
    print('jugador 2 Gana')
elif Jugador2 == 'piedra' and Jugador1 == 'piedra':
    print('Empate')
elif Jugador2 == 'piedra' and Jugador1 == 'papel':
    print('Jugador 1 Gana')
elif Jugador2 == 'papel' and Jugador1 == 'piedra':
    print('Jugador 2 Gana')
elif Jugador2 == 'papel' and Jugador1 == 'tijera':
    print('Jugador 1 Gana')
elif Jugador2 == 'papel' and Jugador1 == 'papel':
    print('Empate')
elif Jugador2 == 'tijera' and Jugador1 == 'piedra':
    print('Jugador 1 Gana')
elif Jugador2 == 'tijera' and Jugador1 == 'tijera':
    print('Empate')
elif Jugador2 == 'tijera' and Jugador1 == 'papel':
    print('Jugador 2 Gana')
else:
    print('Opcion invalida')
