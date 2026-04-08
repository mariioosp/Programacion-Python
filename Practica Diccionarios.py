contactos= {}

while True:
    nombre= input("Introduce el nombre del contacto: ")
    if nombre== 'no':
        break
        
    telefono= input("Introduce el teléfono del contacto: ")
    contactos[nombre] = telefono

print("Agenda de Contactos")
print(contactos)



numeros= []

for i in range(10):
    valor= float(input("Introduce un numero: "))
    numeros.append(valor)

suma_total= sum(numeros)
media= suma_total/ len(numeros)

print("Resultados")
print("Lista de numeros: ", numeros)
print("Suma total: ", suma_total)
print("Media: ", media)
