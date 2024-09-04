total_estudiantes = int(input("Cuántos estudiantes tiene el curso? \n"))
contador = 0
acumulador = 0

while contador < total_estudiantes:
    nota = float(input(f"Ingrese la nota del estudiante {contador + 1}: \n"))
    acumulador += nota
    print(f"Estamos en la iteración {contador + 1} y la suma de las notas hasta ahora es {acumulador} \n")
    contador += 1

promedio = acumulador / total_estudiantes

print(f"El promedio de las notas del curso es {promedio:.2f}")