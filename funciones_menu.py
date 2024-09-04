from ejercicio_sincronico import inventario

def agregar_producto():
    print("A continuación, agrega el producto ingresando los datos solicitados:\n\n")
    nombre_producto = input("Ingresa el nombre del producto: \n")
    precio = int(input("Ingrese el precio del producto: \n"))
    categoria = input("Ingrese la categoría del producto:\n")
    stock = int(input("Ingrese el stock del producto:\n"))

    inventario[nombre_producto] = (categoria,stock,precio)
    return

def buscar_producto():
    while True:
        print("Opciones de búsqueda\n")
        print("1. Buscar por nombre")
        print("2. Buscar por categoría")

        tipo_busqueda = int(input("Ingresa el número de la opción de búsqueda:\n"))

        if tipo_busqueda == 1:
            nombre = input("Ingresa el nombre de producto que deseas buscar")

            if nombre in inventario:
                categoria = inventario[nombre][0]
                stock = inventario[nombre][1]
                precio = inventario[nombre][2]

                print(f"El producto {nombre} es de la categoría {categoria}, su stock es {stock} y su valor es {precio}")
            else:
                print("El producto no se encuentra")
        
        elif tipo_busqueda == 2:
            categoria = input("Escribe la categoría que quieres buscar:\n")

            for clave, valor in inventario.items():
                
                if categoria in valor:
                    nombre_producto = clave
                    stock = valor[1]
                    precio = valor[2]
                    print(f"El producto {nombre_producto} pertenece a la categoría {categoria}, su stock es {stock} y su precio es {precio}")




