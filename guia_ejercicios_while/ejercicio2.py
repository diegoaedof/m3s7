"""numero = int(input("Ingrese un número entero y positivo"))
lista = []
suma = 0

while numero > 0:
    lista.append(int(input("ingresa un entero")))
    numero -= 1
    
for num in lista:
    if num % 2 == 0:
        suma = num + suma
        print(suma)
    else:
        print(0)"""

numero = int(input("ingrese su numero: ")) #6

contador = 1
acumulador = 0


while contador <= numero:
    #print(f"Actualmente el contador vale {contador}")
    #print(f"Actualmente el acumulador vale {acumulador}")

    if contador % 2 == 0:
        acumulador += contador
        
    print(f"Acá finaliza la iteración {contador}")
    contador += 1
    

print("Terminó el ciclo while porque el contador dejó de ser menor o igual al npumero ingresado")

print(f"La suma total de los números pares es {acumulador}")