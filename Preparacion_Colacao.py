print('Me voy a la cocina')
print('Abro la nevera')

leche = input('Hay Leche? (s/n) ')
colacao = input('¿Hay colacao? (s/n) ')


if leche != 's' or colacao != 's':
    print('ir a comprar al super los ingredientes que faltan...')

    if leche != 's':
        print('comprar leche, luego preparar')
    if colacao != 's':
        print('comprar colacao, luego preparar')

print('Primero poner leche en el vaso, luego colocar colacao en el vaso, mezclar')
