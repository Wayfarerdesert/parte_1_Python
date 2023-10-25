
import os

lista_compras = []
input_producto = None

print('\nLista de las Compras!')

while True:
    input_producto = input('\nAñadir a la lista de las compras:.. ([Q para finalizar])\n')
    if input_producto == 'Q':
        break
    elif input_producto in lista_compras:
        print('{} ya esta agregado en la lista.'.format(input_producto))
    else:
        if input('\n¿Seguro que quiere añadir {} a la lista? [S/N] '.format(input_producto)) == 'S':
            lista_compras.append(input_producto)
            print('\n{} se añadio correctamente!'.format(input_producto))
        else:
            print('\n{} no se añadio a tu lista.'.format(input_producto))
    input()
    os.system('cls')

print('\nLa lista de las compras es:')
print(lista_compras)
input()
exit()

