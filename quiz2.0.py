
title =  'Bienvenidos al Test de Geografia'
print('\n' + title + '\n' + '¬' * len(title) + '\n')

puntuacion = 0

question = input('¿Africa es un pais o un continente?\n'
                 'A: Africa es un pais\n'
                 'B: Africa es un continente\n'
                 'C: No se donde esta africa\n')

if question == 'A':
    puntuacion += 0
elif question == 'B':
    puntuacion += 10
elif question == 'C':
    puntuacion += 0
else:
    print('No es una respuesta valida')
    exit()


question = input('¿New York es el pais mas poblado del mundo?\n'
                 'A: Verdadero\n'
                 'B: No sabia\n'
                 'C: Falso, New York es una ciudad no un pais\n')

if question == 'A':
    puntuacion += 0
elif question == 'B':
    puntuacion += 0
elif question == 'C':
    puntuacion += 10
else:
    print('No es una respuesta valida')
    exit()


question = input('¿Cual es el pais mas grande del mundo?\n'
                 'A: Rusia\n'
                 'B: Estados Unidos\n'
                 'C: Brasil\n')

if question == 'A':
    puntuacion += 10
elif question == 'B':
    puntuacion += 0
elif question == 'C':
    puntuacion += 0
else:
    print('No es una respuesta valida')
    exit()

if puntuacion == 30:
    print('\nExelente, has obtenido ' + str(puntuacion) + ' puntos, sigue asi!')
elif puntuacion >= 10 < 30:
    print('\nBien hecho, has conseguido ' + str(puntuacion) + ' puntos!')
else:
    print('\nMejor suerte para la proxima, ' + str(puntuacion) + ' puntos')

