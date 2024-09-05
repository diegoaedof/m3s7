"""
Ingresa el nombre del producto o 'salir' para terminar: manzana
Ingresa la cantidad de manzana: 50 
Ingresa el nombre del producto o 'salir' para terminar: naranja 
Ingresa la cantidad de naranja: 30 
Ingresa el nombre del producto o 'salir' para terminar: salir


Ingresa el nombre del producto que deseas buscar o 'salir' para terminar: manzana 
La cantidad de manzana es: 50 
Ingresa el nombre del producto que deseas buscar o 'salir' para terminar: pera 
Producto no encontrado. 
Ingresa el nombre del producto que deseas buscar o 'salir' para terminar: salir
"""
inventario = {
    "polera":20
}


while True:
    producto = input("Ingrese nombre del producto o 'salir' para terminar: \n").lower()
    if producto == "salir":
        break
    else:
        cantidad = int(input(f"Ingrese la cantidad de {producto}: \n"))
        inventario[producto] = cantidad

while True:
    buscar = input("Ingrese el nombre del producto que deseas buscar o 'salir' para terminar:\n").lower()
    if buscar == "salir":
        break
    else:
        if buscar in inventario:
            print(f"La cantidad de {buscar} es: {inventario[buscar]}")
        else:
            print("Producto no encontrado.")






