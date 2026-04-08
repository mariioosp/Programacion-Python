#EJERCICIO UNO
#palabra=input("Escribe una palabra: ")
#for dato1 in range(40):
    #print(palabra)

#EJERCICIO DOS
#num1=float(input("Escribe un número. Si es 100 se acaba: "))
#while num1!=100:
    #if num1%2==0:
        #print("El número es par")
    #else:
        #print("El numero es impar")
    #num1=float(input("Esbribe otro número: "))
    #if num1==100:
        #print("Se acabó")

#EJERCICIO TRES
#num2=int(input("Escribe un número entero mayor que cero: "))
#if num2> 0:
    #for dato2 in range(num2, -1, -1):
        #if dato2 != 0:
            #print(dato2, end=", ")
        #else:
            #print(dato2)
#else:
    #print("El número debe ser mayor que cero.")

#EJERCICIO CUATRO
#num3=int(input("Escribe un número entero: "))
#for num3 in range(num3+1):
    #print("*" * num3)

#EJERCICIO CINCO
num4=int(input("Escribe un número entero: "))
if num4<= 1:
    print("No es un número primo.")
else:
    primo1=True
    for i in range(2, int(num4**0.5) + 1):
        if num4 % i == 0:
            primo=False
            break
    if primo:
        print("Es un número primo.")
    else:
        print("No es un número primo.")
        
#EJERCICIO SEIS
while True:
    texto=input("Escribe algo (o salir para terminar): ")
    if texto.lower() == "salir":
        print("Programa terminado.")
    print("Eco:", texto)
