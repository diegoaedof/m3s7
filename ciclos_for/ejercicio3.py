
lista = [2,5,63,8,8,5]
acumulador = 0

for numero in range(len(lista)):
    acumulador += lista[numero]

print(f"La suma es {acumulador}")