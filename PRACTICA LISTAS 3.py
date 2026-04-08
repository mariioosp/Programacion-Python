matriz = []
print("Ingrese los valores de la matriz 3x3:")
for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print("Matriz ingresada:")
for fila in matriz:
    print(fila)

suma_total = 0
maximo = matriz[0][0]
minimo = matriz[0][0]

for fila in matriz:
    for elemento in fila:
        suma_total += elemento
        if elemento > maximo:
            maximo = elemento
        if elemento < minimo:
            minimo = elemento

sumas_filas = []
for fila in matriz:
    sumas_filas.append(sum(fila))

print(f"\nSuma total de los elementos: {suma_total}")
print(f"Valor máximo en la matriz: {maximo}")
print(f"Valor mínimo en la matriz: {minimo}")
print(f"Suma de cada fila: {sumas_filas}")
