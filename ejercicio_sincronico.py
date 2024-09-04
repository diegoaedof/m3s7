from funciones_menu import agregar_producto

menu_activo = True
opcion = ""
inventario = {
    "arroz":("abarrote", 5, 1690),
    "pipeño":("alcohol", 100, 4990),
    "granadina":("coctelería", 100, 5390),
    "helado de piña":("helados", 200, 4990),
}

while opcion != 6:
    print("Bienvenidos al Sistema de Gestión de Inventario")
    print("------------------------------------------------")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Mostrar inventario")
    print("6. Salir del programa")
    print("-------------------------------------------------")
    
    opcion = int(input("\n Seleccione una opción escribiendo sólo el número"))

    if opcion == 1:
        agregar_producto()
        
    elif opcion == 2:
        pass
    break
