#DESAFIO ARITMETICO
#OBJETO QUE HAY QUE COGER Y DETERMINAR SI EL USER LO TIENE
#random.randint(1, 100)
import random
print("\n" + "bienvenido al juego de la mazmorra\n" + "-" * len("bienvenido al juego de la mazmorra" + "\n"))
opcion = input("Haz quedado atrapado en latinoamerica tragicamente luego de nacer alli, ya con 16 años "
               "y suficiente dinero para escapar toma una desicion \n"
               "a - Coger un avion \n"
               "b - continuar tu vida en el pais hasta poder irte legalmente sin ningun tipo de necesidad \n")

if opcion == "a":
    print("Por fin, cada vez mas cerca de escapar...")
    opcion = input("primero debes sacar la visa, te tomara 6 meses y medio de espera \n"
          "a - esperar la visa (6 meses y medio) \n"
          "b - esperar a que crezcas y salir sin problemas economicos \n"
          "c - escapar a venezuela donde no necesitas visa \n")
    if opcion == "a":
        print("6 meses mas tarde, vas a tu sita para que te admitan")
        numero_inmigracion = random.randint(1, 100)
        opcion = int(input("El jefe de inmigracion te pregunta una multiplicacion,"
                       "cuanto es  13 * {}?".format(numero_inmigracion)))
        if opcion == (13 * numero_inmigracion):
            print("El jefe de inmigracion se sorprende porque eres inteligente y te da la visa")
            visa_inventario = input("El hombre te mira con cara malisiosa y se acerca a darte la visa \n"
                  "¿tomas la visa (si, no)?")
            if visa_inventario == "si":
                print("coges la visa")
                visa_inventario = True
            else:
               print("no tomas la visa")
               visa_inventario = False

            print("luego de comprar tus voletos de avion te acercas al abordaje")
            print("la asistente de vuelo te pide la visa")
            if visa_inventario == True:
             print("la asistente te deja pasar junto a toda tu familia \n"
                  "porfin salieron de latinoamerica")
            else:
             print(" la asistente nota que no traes la visa y no te permite pasar \n"
                  "no lograste salir de latinomerica \n"
                  "GAME OVER")

        else:
            print("en usa no se permiten idiotas que no saben multiplicar, "
                  "te negan la visa y te quedas en latinoamerica encerrado")
            exit()

    elif opcion == "c":
        print("Alla tu, haz decidido vivir una vida de miseria sin recursos y escasa comida, disfruta el infierno...")
        exit()
    else:
        print("20 años mas tarde.... \n"
        "ya haz crecido y un trabajo estable con buenos ingresos, casa y coche,\n"
              " ademas tienes esposa y (proximamente hijos)")

        opcion = input("¿aun quieres salir de latinoamerica? \n "
                  "Responde (si, no)")

        if opcion == "si":
            opcion = input("primero debes sacar la visa, te tomara 6 meses y medio de espera \n"
                           "a - esperar la visa (6 meses y medio) \n"
                           "b - escapar con tu familia a venezuela donde no necesitas visa \n")
            if opcion == "a":
                print("6 meses mas tarde, vas a tu sita para que te admitan")
                numero_inmigracion = random.randint(1, 100)
                opcion = int(input("El jefe de inmigracion te pregunta una multiplicacion,"
                                   "cuanto es  13 * {}?".format(numero_inmigracion)))
                if opcion == (13 * numero_inmigracion):
                    print("El jefe de inmigracion se sorprende porque eres inteligente y te da la visa")
                    visa_inventario = input("El hombre te mira con cara malisiosa y se acerca a darte la visa \n"
                                            "¿tomas la visa (si, no)?")
                    if visa_inventario == "si":
                        print("coges la visa")
                        visa_inventario = True
                    else:
                        print("no tomas la visa")
                        visa_inventario = False
                    print("luego de comprar tus voletos de avion te acercas al abordaje")
                    print("la asistente de vuelo te pide la visa")
                    if visa_inventario == True:
                        print("la asistente te deja pasar junto a toda tu familia \n"
                                  "porfin salieron de latinoamerica")
                    else:
                        print(" la asistente nota que no traes la visa y no te permite pasar \n"
                                  "no lograste salir de latinomerica \n"
                                  "GAME OVER")
                else:
                    print("en USA no admiten idiotas que no saben multiplicar")
            else:
                print("haz decidido vivir en la pobraza sin recursos, disfruta el infierno...")
        else:
            print("continuas tu vida tranquila y feliz dentro de tu pais luego de aceptar que latinoamerica "
                  "no es un mal lugar :) enjoy...")
            exit()






else:
    print("Una sabia eleccion")

    print("20 años mas tarde.... \n"
          "ya haz crecido y un trabajo estable con buenos ingresos, casa y coche,\n"
          " ademas tienes esposa y (proximamente hijos)")

    opcion = input("¿aun quieres salir de latinoamerica? \n "
              "Responde (si, no)")

    if opcion == "si":
        opcion = input("primero debes sacar la visa, te tomara 6 meses y medio de espera \n"
                       "a - esperar la visa (6 meses y medio) \n"
                       "b - escapar con tu familia a venezuela donde no necesitas visa \n")
        if opcion == "a":
            print("6 meses mas tarde, vas a tu sita para que te admitan")
            numero_inmigracion = random.randint(1, 100)
            opcion = int(input("El jefe de inmigracion te pregunta una multiplicacion,"
                               "cuanto es  13 * {}?".format(numero_inmigracion)))
            if opcion == (13 * numero_inmigracion):
                print("El jefe de inmigracion se sorprende porque eres inteligente y te da la visa")
                visa_inventario = input("El hombre te mira con cara malisiosa y se acerca a darte la visa \n"
                                        "¿tomas la visa (si, no)?")
                if visa_inventario == "si":
                    print("coges la visa")
                    visa_inventario = True
                else:
                    print("no tomas la visa")
                    visa_inventario = False

                print("luego de comprar tus voletos de avion te acercas al abordaje")
                print("la asistente de vuelo te pide la visa")
                if visa_inventario == True:
                    print("la asistente te deja pasar junto a toda tu familia \n"
                          "porfin salieron de latinoamerica")
                else:
                    print(" la asistente nota que no traes la visa y no te permite pasar \n"
                          "no lograste salir de latinomerica \n"
                          "GAME OVER")

            else:
                print("en usa no se permiten idiotas que no saben multiplicar, "
                      "te negan la visa y te quedas en latinoamerica encerrado")
                exit()

        else:
         print("Alla tu, haz decidido vivir una vida de miseria sin recursos y escasa comida, disfruta el infierno...")
         exit()

    else:
        print("continuas tu vida tranquila y feliz dentro de tu pais luego de aceptar que latinoamerica "
              "no es un mal lugar :) enjoy...")
        exit()



print("\n gracias por jugar vuelva pronto")