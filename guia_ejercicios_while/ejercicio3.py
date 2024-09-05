while True:
    edad = int(input("Ingresa una edad entre 18 y 110\n"))
    if 18 <= edad <= 110:
        print("Edad válida")
        break
    else:
        print("La edad no es válida, intente de nuevo.")

