#EJERCICIO 1
num1= int(input("Escriba un número entero: "))
if num1%3==0 or num1%5==0:
    print("El número cumple la condición, es múltiplo")
else:
    print("El número no cumple la condición, no es múltiplo")

#EJERCICIO 3
num2= int(input("Escriba un número entero positivo: "))
for algo in range(num2, -1, -1):
    if algo!= 0:
        print(algo, end= ", ")
    else:
        print(algo)

#EJERCICIO 4
num3= int(input("Escriba un número entero entre el 0 y el 100: "))
if num3>= 0 and num3<= 59:
    print("F")
elif num3>= 60 and num3<= 69:
    print("D")
elif num3>= 70 and num3<= 79:
    print("C")
elif num3>= 80 and num3<= 89:
    print("B")
elif num3>= 90 and num3<= 100:
    print("A")