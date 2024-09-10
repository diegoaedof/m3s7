lista = [2,5,63,8,8,5,1400, 9999, 53,22, 64, 80]

numero = 0

for i in lista:
    if i > numero:
        numero = i
        print("Actualmente el número más grande encontrado hasta ahora es:", numero)

print("-----------\n el mayor numero es", numero)