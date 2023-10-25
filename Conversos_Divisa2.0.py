
libra_euro = float(1.1541)
dollar_euro = 0.8356

opcion = input('\n¿Que moneda desea convertir?\n'
               'A - dollar a euro\n'
               'B - euro a dollar\n'
               'C - libra a euro\n'
               'D - euro a libra\n')

texto_usuario = '\n¿Cuantos {} desea convertir?\n'


if opcion == 'A':
    monto = float(input(texto_usuario.format('USD')))
    print(('\nSu cambio es: ' + str(monto * dollar_euro / 1.0) + ' EUR'))

elif opcion == 'B':
    monto = float(input(texto_usuario.format('EUR')))
    print(('\nSu cambio es: ' + str(monto / dollar_euro / 1.0) + ' USD'))

elif opcion == 'C':
    monto = float(input(texto_usuario.format('GBP')))
    print(('\nSu cambio es: ' + str(monto * libra_euro / 1.0) + ' EUR'))

elif opcion == 'D':
    monto = float(input(texto_usuario.format('EUR')))
    print(('\nSu cambio es: ' + str(monto / libra_euro / 1.0) + ' GBP'))

else:
    print('La entrada recibida no es correcta')
