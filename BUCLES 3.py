#EJERCICIO 1
print("FOR:")
for num1 in range(1, 101):
    print(num1)

print("WHILE:")
num2 = 1
while num2 <= 100:
    print(num2)
    num2 += 1

#EJRCICIO 2
suma = 0
num3 = 0
while num3 >= 0:
    num3 = int(input("Escriba un número entero positivo (negativo para terminar): "))  
    if num3 >= 0:
        suma += num3
        print("Suma= ", suma)
    else:
        print("Fin del programa.")
        print("Suma total= ", suma)

#EJRCICIO 3
opcion = 0
while opcion != 4:
    print("MENÚ")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a + b)
    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a - b)
    elif opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a * b)
    elif opcion == 4:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intenta de nuevo.")
