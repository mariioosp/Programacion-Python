num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Ambos números son iguales.")


if num1 > num2:
    print(f"El número mayor es: {num1}")
    suma = float(input("Introduce un valor para sumar al número mayor: "))
    resultado_mayor = num1 + suma
    print(f"El resultado de sumar {suma} al número mayor es: {resultado_mayor}")

    print(f"El número menor es: {num2}")
    multiplicador = float(input("Introduce un valor para multiplicar al número menor: "))
    resultado_menor = num2 * multiplicador
    print(f"El resultado de multiplicar {num2} por {multiplicador} es: {resultado_menor}")

elif num2 > num1:
    print(f"El número mayor es: {num2}")
    suma = float(input("Introduce un valor para sumar al número mayor: "))
    resultado_mayor = num2 + suma
    print(f"El resultado de sumar {suma} al número mayor es: {resultado_mayor}")

    print(f"El número menor es: {num1}")
    multiplicador = float(input("Introduce un valor para multiplicar al número menor: "))
    resultado_menor = num1 * multiplicador
    print(f"El resultado de multiplicar {num1} por {multiplicador} es: {resultado_menor}")

else:
    print("Los dos números son iguales, no se realizan operaciones.")