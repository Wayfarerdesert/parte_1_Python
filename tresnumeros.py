# hacer un programa donde haya que introducir 3 numeros y que el programa nos diga cual es el mas grande y cual es el mas pequeño
intro = 'Hola, este es el juego 3 numeros'
print(intro)

name = input('¿como te llamas?')
print('Hola ' + name)

rules = 'Debes elegir tres numeros y yo te dire cual es el mas alto y cual es el mas bajo'
print(rules)

number_1 = int(input('dime el primer numero: '))
number_2 = int(input('muy bien, ahora dime el segundo numero: '))
number_3 = int(input('muy bien, dime el ultimo numero que has escogido: '))


answer_1 = str(max(number_1, number_2, number_3))
answer_2 = (min(number_1, number_2, number_3))
print(('el numero mas alto que has elegido es '+ answer_1),
      (', y el numero mas bajo que has elegido es {}.'.format(answer_2))
      )


salute = 'muy bien, hemos acabado. Hasta pronto'

final_question = input('¿Estoy en lo correcto?: y/n ')
if final_question == 'y':
    print(salute)
else: print('Debo estudiar matematicas')






