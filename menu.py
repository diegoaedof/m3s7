opcion = ""

while True:
    print("\n \nBienvenido al menú de opciones")
    print("------------------------------")
    print("Seleccione una opción, ingresando sólo el número\n")
    print("1- Inicio de sesión", "2- Registrarse", "3- Publicar", "4- Salir", sep="\n")

    opcion = int(input("Seleccione el número\n"))

    if opcion == 1:
        print("Bienvenido al inicio de sesión")
    elif opcion == 2:
        print("Bienvenido al registro")
    elif opcion == 3:
        print("En este lugar puedes publicar posts")

        while True:
            print("\n \nOpciones de publicación")
            print("------------------------------")
            print("Seleccione una opción, ingresando sólo el número\n")
            print("1- Foto", "2- Video", "3- Texto", "4- Salir", sep="\n")

            sub_opcion = int(input("Seleccione el número\n"))

            if sub_opcion == 1:
                print("Publicaste una foto")
            elif sub_opcion == 2:
                print("Publicaste un video")
            elif sub_opcion == 3:
                print("Publicaste un texto")
            elif sub_opcion == 4:
                break
            else:
                print("Ingresa una opción válida")

    elif opcion == 4:
        break
    else:
        print("Ingrese una opción válida.")

print("Has salido del menú correctamente.")