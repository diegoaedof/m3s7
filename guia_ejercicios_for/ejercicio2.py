suma_par = 0
suma_impar = 0

for i in range(1,51):
    if i % 2 == 0:
        suma_par += i
    else:
        suma_impar += i

print(f"La suma de los pares entre 1 y 50 es {suma_par}")
print(f"La suma de los impares entre 1 y 50 es {suma_impar}")