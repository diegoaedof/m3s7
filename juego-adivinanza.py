import random

numero_correcto = random.randint(1,10) #8
adivinado = False

while not adivinado:
    respuesta = int(input("Ingresa un número del 1 al 10\n"))

    if respuesta == numero_correcto:
        print(f"Ganaste! El número correcto es {numero_correcto}")
        adivinado = True
    elif respuesta < numero_correcto:
        print("El número que ingresaste es menor que el número correcto.")
    else:
        print("El numero que ingresaste es mayor que el número correcto")

