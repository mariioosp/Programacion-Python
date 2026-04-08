numero = int(input("Introduce un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

texto1 = input("Introduce el primer texto: ")
texto2 = input("Introduce el segundo texto: ")
texto3 = texto1 + " " + texto2
print(f'"{texto1}", "{texto2}", "{texto3}"')

nota = float(input("Introduce la nota de la asignatura de Programación en Python: "))
if nota >= 5:
    print("Has aprobado.")
else:
    print("Has suspendido.")
