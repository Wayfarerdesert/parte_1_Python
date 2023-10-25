# hacer un programa en el cual el usuario tiene q averigual un numero del 1 al 10
# si e numero es igual gana. si no termina el juego.

import random
winner_number = random.randint(1, 10)

print('Adivina el numero')
user_number = int(input('Elija un numero del 1 al 10 '))


if user_number == winner_number:
    print('Bien hecho, has ganado')
else: print('El numero ganador era: {} Game Over'.format(winner_number))

