alumnos = ["jose","jonathan","marco"]

print(alumnos)

for i in alumnos:
    print(i + "...ok ")

print("fin")

import csv

# Ruta absoluta
# NUNCA USAMOS RUTAS ABSOLUTAS
# Van en contra de la reproducibilidad
# archivo = open("c:/documentos/users/josemanuel/data/nextlix.csv")

# Rutas relativas
# Le decimos a la computadora "como navegar" hasta el archivo

# Esto no debemos hacerlo nunca, porque abrimos una conexión al archivo
# y se nos puede olvidar cerrar la conexión
# archivo = open("./data/01nextlix.csv").readlines()

# Esto cierra en automático la conexión al archivo cuando llega al final del bloque de código
with open("./data/01netflix.csv", encoding="UTF-8") as archivo:
#with open("./data/01netflix.csv", encoding="latin1") as archivo:
#    data = archivo.readlines()
#    print(data[0])

    reader = csv.reader(archivo, delimiter=",")

    encabezado = next(reader)
    print(encabezado)

    for i in reader:
        # Listar programas y su rating
        programa = i[0]
        rating = i[5]

        if rating.isdigit(): # Método de strings
            rating = int(rating)
            if rating >= 90:
                print(f"Programa: {programa}, Rating: {rating}")