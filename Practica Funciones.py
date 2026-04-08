#TAREA 1
def primo():
    num1= int(input("Ingrese un número: "))
    if num1<= 1:
        return False
    for i in range(2, num1):
        if num1%i== 0:
            print("No es primo")
            break
        else:
            print("Es primo")
primo()

#TAREA 2
def listas_son_iguales(lista1, lista2):
    if len(lista1) != len(lista2):
        return False
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
            return False
    return True
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 4]

print(listas_son_iguales(a, b))
print(listas_son_iguales(a, c))
