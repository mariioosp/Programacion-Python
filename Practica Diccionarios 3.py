alumnos = {
    "Ana": {"edad": 20, "nota": 8.5},
    "Luis": {"edad": 22, "nota": 6.0},
    "Marta": {"edad": 19, "nota": 9.5}
}
suma_notas = 0
mejor_nota = -1
mejor_alumno = ""

print("--- LISTADO DE ALUMNOS ---")

for nombre, datos in alumnos.items():
    edad = datos["edad"]
    nota = datos["nota"]
    
    print("Alumno: ",nombre," | Edad: ",edad," | Nota: ",nota)
    
    suma_notas += nota
    
    if nota > mejor_nota:
        mejor_nota = nota
        mejor_alumno = nombre

media = suma_notas / len(alumnos)

print("Nota media de la clase: ",media)
print("El alumno con la nota más alta es ",mejor_alumno," con un ",mejor_nota)
