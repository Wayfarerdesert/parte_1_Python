edad = int(input('Digame su edad: '))
tipo_de_carnet = input('Digame su tipo de carnet (E para Estudiante / '
                       'P Pensionista / F Familia numerosa / N Ninguno): ')

if (25 >= edad <= 35 and tipo_de_carnet == 'E' or 'e') or \
        edad <= 10 or \
        (edad >= 65 and tipo_de_carnet == 'P' or 'p') or \
        (tipo_de_carnet == 'F' or 'f'):
    print('Se te aplica el descuento del 25%')

else:
    print('No se aplica el descuento')
