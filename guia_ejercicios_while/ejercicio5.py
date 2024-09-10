from os import system

inventario = {}

while True:
    print("Menú de gestión de inventario")
    print("------------------------------")
    print("1. Agregar producto")
    print("2. Actualizar cantidad")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Salir")

    opcion = int(input("Selecciones una opción ingresando el número:\n"))

    if opcion == 1:
        #instrucciones para agregar producto
        #Se solicita ingreso de datos al usuario
        producto = input("Ingrese un nombre de producto:\n")
        if producto in inventario:
            print(f"{producto} ya existe en el inventario.")
        else:
            cantidad = int(input("Ingresa la cantidad del producto: \n"))
            #Se crea la clave y se asigna un valor en el diccionario
            inventario[producto] = cantidad
            #Se muestra un mensaje de confirmación al usuario
            print(f"Producto {producto} fue añadido exitosamente. ")
    elif opcion == 2:
        #instrucciones para actualizar la cantidad
        producto = input("Ingrese un nombre de producto a actualizar:\n")
        if producto in inventario:
            cantidad = int(input("Ingresa la cantidad actualizada del producto: \n"))
            inventario[producto] = cantidad
            print(f"La cantidad de {producto} fue actualizada correctamente.")
        else:
            print("El producto ingresado no se encuentra en el inventario.")
    elif opcion == 3:
        #instrucciones para eliminar producto
        producto = input("Ingresa el nombre del producto que quieres eliminar.\n")
        if producto in inventario:
            del inventario[producto]
        else:
            print("El producto no existe en el inventario.")

    elif opcion == 4:
        #instrucciones para mostrar invwentario
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("Productos            Cantidad")
            productos = list(inventario.keys())
            cantidades = list(inventario.values())
            indice = 0

            while indice < len(productos):
                print(f"{productos[indice]}      :      {cantidades[indice]}")
                indice += 1

    elif opcion == 5:
        print("Has salido del menú.")
        break
    else:
        print("Por favor, ingresa un número entre 1 y 5.")
    
    input("Presione Enter para continuar.")
    system("clear")


