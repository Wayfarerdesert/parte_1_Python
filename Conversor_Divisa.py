libra_euro = float(1.1541)
# euro_libra = float(0.8665)
monto = float(input('¿Cuantas libras desea cambiar?: '))

print('Su cambio es de ' + str(monto * libra_euro / 1.0) + 'EUR')
