print('\nBienvenidos al Phone Shelter')
print('Te ayudare a elgir lael movil correcto para ti')

sistema_operativo = input('\n¿Que sistema operativo prefieres?\n'
                          'A - Android\n'
                          'B - iOS\n')

movil_ideal = 'No hemos encontrado el movil adecuado para ti'


if sistema_operativo == 'A' or 'a':
    dinero = input('\n¿Tienes dinero?\n'
                   'A - Mi presupuesto es muy bajo\n'
                   'B - Si, eso no es un problema\n')

    if dinero == 'A' or 'a':
        movil_ideal = 'Android chino 100€'


    else:
        camara_photo = input('\n¿Te inporta la camara del movil\n'
                             'A - si, es muy importante\n'
                             'B - No, en absoluto\n')

        if camara_photo == 'A' or 'a':
            movil_ideal = 'Google pixel supercam'
        elif camara_photo == 'B' or 'b':
            movil_ideal = 'Android calidad precio'

elif sistema_operativo == 'B' or 'b':
    dinero = input('\n¿Tienes dinero?\n'
                   'A - Mi presupuesto es muy bajo\n'
                   'B - Si, eso no es un problema\n')

    if dinero == 'A' or 'a':
        movil_ideal = 'Iphone de segunda mano'


    else:
        camara_photo = input('\n¿Te inporta la camara del movil\n'
                             'A - si, es muy importante\n'
                             'B - No, en absoluto\n')

        if camara_photo == 'A' or 'a':
            movil_ideal = 'Iphone Ultra pro max'
        elif camara_photo == 'B' or 'b':
            movil_ideal = 'Iphone ultra'


else:
    print('No es una respuesta valida\n')
    exit()

print('\nEl movil mas adecuado para ti es: ' + movil_ideal)
