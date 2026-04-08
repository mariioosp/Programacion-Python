tareas= []

opcion= ""

while opcion!= "4":

    print("MENÚ")
    print("1. Añadir una tarea")
    print("2. Eliminar una tarea")
    print("3. Mostrar todas las tareas")
    print("4. Salir")

    opcion= input("Elige una opción: ")

    if opcion == "1":
        tarea= input("Cuál es el nombre de la tarea: ")
        tareas.append(tarea)
        print("Tarea añadida a la lista")

    elif opcion == "2":
        eliminar= input("Cuál es el nombre de la tarea que quiere eliminar: ")
        tareas.remove(eliminar)
        print("Tarea eliminada de la lista")

    elif opcion== "3":
        print(tareas)
        
    if opcion== "4":
        print("Saliendo del programa")

    
    
