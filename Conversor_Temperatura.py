print('Bienvenido al convertor de temperatura')

grados_Fahrenheit = float(input('Temperatura en Fº '))
grados_Celcius = (grados_Fahrenheit - 32) * 5 / 9

print(('La temperatura en Celcius es de ') + str(grados_Celcius) + ' Cº')
