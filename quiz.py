
title = 'Bienvenidos al Rugby Test'
print('\n' + title + '\n' + '-' * len(title) + '\n')

puntuacion = 0

opcion = input('''Pregunta 1: El rugby es tu deporte favorito? 
A - Es mi deporte favorito
B - Me agrada pero no es mi deporte favorito
C - Lo detesto''')

if opcion == 'A':
    puntuacion = puntuacion + 10
elif opcion == 'B':
    puntuacion += 5
elif opcion == 'C':
    puntuacion += 0
else:
    print('\nNo es una respueta valida')
    exit()


opcion = input('\nPregunta 2: Juegas al Rugby? \n'
               'A - Si, hace años\n'
               'B - Si, estoy recien comenzando\n'
               'C - No, tengo cosas mas interesantes que hacer\n')

if opcion == 'A':
    puntuacion = puntuacion + 10
elif opcion == 'B':
    puntuacion += 5
elif opcion == 'C':
    puntuacion += 0
else:
    print('\nNo es una respueta valida')
    exit()


opcion = input('\nPregunta 3: Cual es el puesto en el que juegas? \n'
               'A - Forward\n'
               'B - Backs\n'
               'C - Wing\n')

if opcion == 'A':
    puntuacion = puntuacion + 10
elif opcion == 'B':
    puntuacion += 5
elif opcion == 'C':
    puntuacion += 0
else:
    print('\nNo es una respueta valida')
    exit()


if puntuacion >= 25:
    print('\nEnahorabuena, eres fan del Rugby')
elif puntuacion >= 15:
    print('\nFelicidades, el Rugby es tu deporte favorito')
else:
    print('\nEl Rugby no es un deporte adecuado para ti')
