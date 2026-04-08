#1. Listas

notas = []
veces = int(input("Número de notas que queremos introducir: "))

for i in range(veces):
    while True:
        nota = float(input(f"Introduzca la nota del alumno (0-10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Error: La nota debe estar entre 0 y 10. Inténtalo de nuevo.")
print(notas)

suma_total= sum(notas)
cantidad= len(notas)
media= suma_total / cantidad
print("La nota media es: ", media)

nota_maxima= max(notas)
print("La nota más alta es: ", nota_maxima)

nota_minima= min(notas)
print("La nota más baja es: ", nota_minima)

#2. Diccionarios

contactos = {}
nombre1= input("Escriba un nombre para su primer contacto: ")
nombre2= input("Escriba otro nombre para su segundo contacto: ")
telefono1= int(input("Escriba un teléfono para su primer contacto (9 dígitos): "))
telefono2= int(input("Escriba otro teléfono para su segundo contacto (9 dígitos): "))

contactos[nombre1]= telefono1
contactos[nombre2]= telefono2

busqueda= input("Escriba el nombre del contacto que quieres buscar: ")
if busqueda == nombre1:
    print(contactos.get(nombre1))
elif busqueda == nombre2:
    print(contactos.get(nombre2))
else:
    print("El contacto que quiere buscar no existe")

print(contactos)

borrar = input("Escriba el nombre del contacto a eliminar: ")
if borrar in contactos:
    del contactos[borrar]
    print("El contacto ",borrar, " eliminado correctamente")
else:
    print("No se pudo eliminar: el nombre no existe")
print(contactos)

#3. Tuplas

coordenadas = ()

print("Introduce 5 coordenadas (x, y):")

for i in range(5):
    x = float(input("Escribe X: "))
    y = float(input("Escribe Y: "))
    
    punto_actual = (x, y)
    coordenadas = coordenadas + (punto_actual,)
        
print(coordenadas)

contador_primer_cuadrante = 0
for p in coordenadas:
    if p[0] > 0 and p[1] > 0:
        contador_primer_cuadrante = contador_primer_cuadrante + 1
print("Coordenadas en el primer cuadrante: ",contador_primer_cuadrante)

#4. Funciones

def funciones():
    print("-----MENÚ-----")
    print("Suma")
    print("Resta")
    print("Multiplicación")
    print("División")
    num1= float(input("Escriba un número para la operación: "))
    num2= float(input("Escriba otro número para la operación: "))
    operacion= input("¿Qué operación quiere ver? ")

    suma= num1 + num2
    resta= num1 - num2
    multiplicacion= num1 * num2
    division= num1 / num2

    if operacion == "Suma":
        print("La suma de ",num1, " + ",num2," es = ", suma)
    elif operacion == "Resta":
        print("La resta de ",num1, " - ",num2," es = ", resta)
    elif operacion == "Multiplicacion":
        print("La multiplicación de ",num1, " * ",num2," es = ", multiplicacion)
    elif operacion == "Division":
        if num2 != 0:
            print("La division de ",num1, " / ",num2," es = ", division)
        else:
            print("Error: No se puede dividir entre cero")

funciones()

   
    





































