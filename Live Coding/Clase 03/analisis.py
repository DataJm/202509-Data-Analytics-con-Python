"""
El truco de las triples "double quotes" es para poder escribir documentación
o comentarios en Python y que sea un poco más comoda la escritura
"""

# También puedo usar el "#" para escribir comentarios o documentación
# pero entonces tengo que iniciar cada nueva linea con el simbolo "#"

"""
Reto: Leer y analizar el dataset de audi.csv
- Calcular el precio promedio de cada modelo dentro del archivo CSV
- 1 Leer el archivo CSV
- 2 Iterar por cada fila del archivo
- 3 Guardar el modelo en un diccionario y acumular la suma del precio además del conteo de cada modelo
- 4 Calcular el promedio para cada modelo
- 5 Exportar los resultados a un archivo CSV

- BONUS: Hacerlo con funciones
"""
import csv

archivo_fuente = './data/02audi.csv'
archivo_de_salida = "./Live Coding/Clase 03/resultados.csv"

with open(archivo_fuente) as archivo:
    # Este código no tiene dependencias, lee todo el contenido del archivo al mismo tiempo
    # lineas = archivo.readlines()
    # print(lineas)

    # Si mi archivo no tuviera encabezados, preferiría usar csv.reader en vez de Dict
    # reader = csv.reader(archivo, delimiter=",")
    # for fila in reader:
    #   print(fila)
    #   modelo = fila[0]

    reader = csv.DictReader(archivo)
    print(reader.fieldnames) # reader.fieldnames es el header del archivo CSV, asume que los encabezados están ahí

    suma_por_modelo = {}
    conteo_por_modelo = {}

    for fila in reader:
        modelo= fila.get("model")
        precio= fila.get("price")
        precio= float(precio)
        # print(modelo, precio) # En python, es posible enviar más de 1 objeto a print, y los imprime en una misma linea
        if modelo in suma_por_modelo:
            # Escenario cuando el modelo ya fue visto anteriormente
            suma_por_modelo[modelo] = suma_por_modelo[modelo] + precio
            conteo_por_modelo[modelo] = conteo_por_modelo[modelo] + 1
        else:
            # Escenario cuando el modelo es visto por primera vez
            suma_por_modelo[modelo] = precio
            conteo_por_modelo[modelo] = 1 

# Finalizamos la indentación, ya podemos cerrar el archivo de audi.csv
promedio_por_modelo = {}
for modelo in suma_por_modelo:
    suma_precio = suma_por_modelo[modelo]
    conteo = conteo_por_modelo[modelo]
    promedio_por_modelo[modelo] = suma_precio / conteo

# print(promedio_por_modelo.items())

# Exportar los resultados
# Necesito pasarle permisos explicitos de escritura : "w"
with open(archivo_de_salida, "w") as resultados:
    
    writer = csv.writer(resultados)

    for modelo in promedio_por_modelo:
        # Al writer, con el método writerow le tengo que pasar una lista con lo que escribiré en cada fila del CSV
        writer.writerow([modelo, promedio_por_modelo[modelo]])
