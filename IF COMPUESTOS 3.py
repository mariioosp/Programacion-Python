edad = int(input("Introduce tu edad: "))
altura = int(input("Introduce tu altura en centímetros: "))

if altura < 140:
    if edad < 12:
        print("Puedes acceder a las atracciones infantiles.")
    else:
        print("No puedes acceder a ninguna atracción debido a la restricción de altura.")
elif 140 <= altura <= 170:
    if edad < 12:
        print("Puedes acceder a las atracciones familiares.")
    else:
        print("Puedes acceder a las atracciones familiares y a las montañas rusas de intensidad media.")
else:
    if edad < 12:
        print("Puedes acceder a las atracciones familiares y a las montañas rusas de intensidad media.")
    else:
        print("Puedes acceder a todas las atracciones del parque, incluidas las de alta intensidad.")
