#EJERCICIO 1
contactos= []
hola= input("Agrega un contacto con nombre y número de teléfono: ")
contactos.append(hola)

adios= input("Que contacto por su nombre quiere eliminar: ")
contactos.remove(adios)

hoy= input("Que contacto por su nombre quiere buscar: ")
print(hoy)
print(len(hoy))
print(contactos)
   
#EJERCICIO 2
calificaciones= []
calificaciones.append(9.25)
calificaciones.append(6)
calificaciones.append(4.2)
calificaciones.append(8)
calificaciones.append(3.4)
calificaciones.append(1.7)
calificaciones.append(5)
print(calificaciones)
print(sum(calificaciones)/len(calificaciones))
print(max(calificaciones))
print(min(calificaciones))
#EJERCICIO 3
palabra= input("Escriba una palabra: ")
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
