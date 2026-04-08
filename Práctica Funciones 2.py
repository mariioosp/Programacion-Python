#1.
def calcular_precio_final(precio, descuento):
    precio_final= precio - (precio * descuento / 100)
    return precio_final
precio= int(input("Escriba un valor para el precio: "))
descuento= int(input("Escriba un valor para el descuento: "))
resultado1= calcular_precio_final(precio, descuento)
print("El precio con el descuento aplicado en él es:", resultado1)

#2.
def area_rectangulo(base, altura):
    area= base * altura
    return area
base=int(input("Escriba un valor para la base: "))
altura= int(input("Escriba un valor para la altura: "))
resultado2= area_rectangulo(base, altura)
print("El resultado del área del rectángulo es:", resultado2)

#3.
def celsius_a_fahrenheit(celsius):
    fahrenheit= celsius * 1.8 + 32
    return fahrenheit
celsius= int(input("Escriba un valor para los grados celsius: "))
resultado3= celsius_a_fahrenheit(celsius)
print(celsius,"ºC son equivalentes a", resultado3,"F")

#4.
def contar_letra(texto, letra):
    return texto.count(letra)
texto= input("Escriba una palabra cualquiera: ")
letra= input("Escriba una letra cualquiera: ")
resultado4= contar_letra(texto, letra)
print("La palabra", texto,"tiene", resultado4,"letra/s", letra)

#5.
def calcular_media(nota1, nota2, nota3):
    media= (nota1 + nota2 + nota3) / 3
    if media >= 5:
        print("Aprobado")
    else:
        print("Suspenso")
    return media
nota1= float(input("Esriba una nota: "))
nota2= float(input("Esriba otra nota: "))
nota3= float(input("Esriba otra nota: "))
resultado5= calcular_media(nota1, nota2, nota3)

