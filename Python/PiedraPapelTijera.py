Jugador1 = input('Escoge una opcion [1] Piedra [2] Papel [3] Tijera: ')
Jugador2 = 'Piedra'

if Jugador1 == Jugador2 or Jugador1 == 'piedra':
    print('Empate')
elif Jugador1 == 'Tijera' or Jugador1 == 'tijera':
    print('Perdiste')
elif Jugador1 == 'Papel' or Jugador1 == 'papel':
    print('Ganaste')
else:
    print('Opcion invalida')