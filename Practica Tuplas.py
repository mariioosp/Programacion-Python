valores1= (3, 56, 43, 18)
valores2= (98, 28, 4, 23)


suma = tuple(valores1[i] + valores2[i] for i in range(4))
resta = tuple(valores1[i] - valores2[i] for i in range(4))
producto = tuple(valores1[i] * valores2[i] for i in range(4))


print("Resultados de las Operaciones")

print("Suma de posiciones:")
for val in suma:
    print("Resultado suma: ", suma)

print("Resta de posiciones:")
for val in resta:
    print("Resultado resta: ", resta)

print("Producto de posiciones:")
for val in producto:
    print("Resultado producto: ", producto)
