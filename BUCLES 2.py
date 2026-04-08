#EJERCICIO 1
num1 = 0
while num1!= 10:
    for num1 in range(1, 11):
        resultado =2 * num1
        print('2 *', num1, '=', resultado)
#EJERCICIO 2
num2 = 0
num3 = 1
print(num2)
print(num3)
for i in range(8):
    c = num2 + num3
    print(c)
    num2 = num3
    num3 = c
#EJERCICIO 3
num4 = 1
for i in range(1, 16):
    num4 = num4 * i
print(num4)
#EJERCICIO 4
while True:
    num5 = int(input("Introduce un número entre 0 y 999 (0 para salir): "))
    if num5 == 0:
        print("Fin del juego.")
        break
    if num5 < 0 or num5 > 999:
        print("Número fuera de rango. Intenta de nuevo.")
        continue
    digitos = len(str(num5))
    print("El número tiene", digitos, "dígito(s).")
