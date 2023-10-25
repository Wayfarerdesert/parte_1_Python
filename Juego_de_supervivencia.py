import random

print('\nJuego de supervivencia\n'
      '-----------------------\n'
      'El año 2020 te pego duro, te has quedado sin trabajo a raiz de la llegada del covid\n'
      '2019, el virus que parece acabara con la humanidad. Luego de unos meses de cuarentena\n'
      'en la habitacion de tu piso, finalmente las autoridades te dejan salir a la calle, y\n'
      'tu comienzas nuevamente a rehacer tu vida. Cuando comienzas a caminar nuevamente por\n'
      'las calles te acuerdas que el sol existe, conoces nuevas personas vas a caminar a la\n'
      'playa, disfrutas del momento. Decides cambiar de piso y conoces a X, una persona guay\n'
      'con quien te haces amigo y despues de un tiempo resulta que se convirtio en el amor\n'
      'de tu vida. Todo continua bien hasta que un dia empiezas a notar que las restricciones\n'
      'y el control debido al covid no disminuyen y piensas que todo sigue medio jodido.\n'
      'Es en eso momento cuando tu junto a X comienzan a penzar cual sera el rumbo que tomen\n'
      'sus vidas.\n'
      '\nLuego de analizarlo llegan a la conclusion de que tienen dos posibilidades:')

opcion = input('a - Seguir viviendo en europa y esperar que todo mejore.\n'
               'b - Viajar hacia america con la intencion de ahorrar algo de dinero y\n'
               '    vovler a europa cuando el virus se haya acabado.\n')

if opcion == 'a':
    print('Deciden seguir viviendo en europa, pero deben empezar a ahorrar dinero.\n'
          '¿que hacen?')
    opcion = input('a - Nada, seguir en el mismo piso y esperar que todo mejore pronto.\n'
                   'b - Buscar un piso mas pequeño.\n'
                   'c - Buscar un trabajo.\n')

    if opcion == 'a':
        print('Deciden seguir viviendo en el mismo piso y con la ayuda del estado, pero\n'
              'no consideraron que el estado no les pagaria mas y que el covid seguiria\n'
              'por mucho tiempo, por lo que luego de 3 meses se quedan sin dinero, deben\n'
              'dejar el piso y terminan viviendo en la calle.\n'
              'FIN')

    elif opcion == 'b':
        print('Luego de una busqueda exaustiva han encontrado un piso mas pequeno y economico\n'
              'que le agrada pero esta ubicado en otra ciudad, por lo que estaran lejos de sus\n'
              'amigos y familia.')
        opcion = input('¿lo rentan si o no?\n')

        if opcion == 'si':
            print('Deciden rentar el piso mas pequeño con la esperanza de poder ahorrar dinero y\n'
                  'de que estaran alli por poco tiempo. Pero finalmente el estado de alarma debido\n'
                  'al covid se prolongo demasiado tiempo, y tu y X se terminaron peleando debido a\n'
                  'la mala desicion que tomar al ir a ese piso, dejan el piso y terminan si relacion.\n'
                  'FIN\n')

        elif opcion == 'no':
            print('Finalmente no cogieron ese piso porque no les gustaba que fuera en otra ciudad,\n'
                  'por lo que deciden quedarse donde estan y ahorrar dinero de otras formas. Luego\n'
                  'de unos meses la situacion del covid comienza a mejorar, ambos consiguen trabajo\n'
                  'y siguen felices de haber tomado la desicion correcta.\n')

        else:
            print('No has elgido la opcion correcta')
            exit()

    elif opcion == 'c':
        print('Luego de una ardua busqueda de trabajo finalmente lo consiguen, estan contentos,\n'
              'pero luego de un tiempo les informan que seran despedidos de sus trabajos y\n '
              'analizando todo nuevamente se dan cuenta que la mejor opcion que tienen para ahorrar\n'
              'dinero es el viaje temporal a latinoamerica donde la vida es mas economica.\n')

    else:
        print('No has elgido la opcion correcta')
        exit()

elif opcion == 'b':
    print('Han decidido arriesgarce y hacer el viaje, ya han elegido a que pais iran y han\n'
          'comenzado a empacar y a buscar todo el papeleo.\n'
          '\nAhora deden decidir que hacer con todas sus cosas.\n')
    opcion = input('a - Empacar poco, viajar liviano y rentar un trastero grande y mas costoso\n'
                   '    para dejar el resto de cosas.\n'
                   'b - Empacar la mayor cantidad de cosas posibles, vender lo que no usan y\n '
                   '    rentar un trastero mas pequeño y economico para dejar el resto de cosas.\n')

    equipaje = False

    if opcion == 'a':
        print('Viajas Liviano\n')
        equipaje = True

    elif opcion == 'b':
        print('Empacas todo\n')

    else:
        print('No has elgido la opcion correcta')
        exit()


    dia_random = random.randint(1, 22)
    dia_del_viaje = random.randint(23, 31)

    print('Una vez decidido que hacer con todas las cosas de la casa, y luego de haber comprado\n'
          'el vuelo, deben calcular bien cuantos dias tienen para terminar de empacar.\n'
          'Si hoy es el dia numero ', dia_random, 'y viajan el dia ', dia_del_viaje)

    opcion = int(input('¿cuantos dias les quedan para terminar de empacar?\n'))
    if opcion == dia_del_viaje - dia_random and equipaje:
        print('Finalmente consiguieron empacar todo y dejar el piso a tiempo, y como habian\n'
              'decidido viajar liviano, al llegar a la aduana de el pais destino el oficial\n'
              'de seguridad los deja pasar sin problemas. Finalmente lo han conseguido!!!\n'
              'Felicitaciones.')


    elif opcion == dia_del_viaje - dia_random:
        print('Finalmente consiguieron empacar todo y dejar el piso a tiempo, pero como han decidido\n'
              'viajar con la mayor cantidad de cosas posibles, al  llegar a la aduana de el pais destino\n'
              'el oficial de seguridad los mira raro por tanto equipaje y les pregunta cuantos dias piensan\n'
              'quedarse en el pais?')

        dias_del_visado = 90

        tiempo_de_estadia = int(input())
        if tiempo_de_estadia <= dias_del_visado:
            print('Consiguieron convenser al oficial de que se quedarian el tiempo que su visa les permite\n'
                  'y los deja pasar sin problemas. Finalmente lo han conseguido!!!\n'
                  'Felicitaciones.')

        else:
            print('Como le dijeron al oficial que pretendian quedarse en el pais mas de los dias que su visa\n'
                  'les permite, este les denego la entrada y los envio de nuevo a su pais.\n'
                  'FIN')


    elif opcion != dia_del_viaje - dia_random:
        print('Debido a que calcularon mal los dias que les quedaban para terminar de emepacar,\n'
              'les han quedado cosas por hacer, perdieron el vuelo y se quedaron sin el piso.\n'
              'FIN')


else:
    print('No has elgido la opcion correcta')
    exit()
