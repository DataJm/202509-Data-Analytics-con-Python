texto = "Hola Python"

print(texto.upper()) # Una función que vive dentro de un objeto : método
# upper() -> Esta función por si sola no existe 

print() # Esto es una función. No nace de un objeto


# Tipos de dato

# Numeros
edad = 39
# String
nombre = "Manuel"
# Boleanos
instructor = True

print("Mi nombre es Jose")
print("Mi nombre es " + nombre)

# f-string template
print(f"Mi nombre es {nombre}")

print(f"""
--------------------
Hola, mi nombre es {nombre},
tengo {edad} años
Y a la pregunta, soy instructor? Pues {instructor}
--------------------
""")

# Operador de suma

resultado = 2 + 2 
print(resultado)

# Listas

alumnos = ["Ana","Jose","Bruno"]
print(alumnos)

alumnos_tupla = ("Ana","Jose","Bruno")
print(alumnos_tupla)

# Lista vs Tupla
# Ambas son ordenadas y tienen indice
# NOTA: En python, los indices empiezan en 0 , el primer elemento siempre es el elemento 0 
print(alumnos[0])
print(alumnos_tupla[0])

# Agregar items a una lista
alumnos.append("Antonio") # Método Append

print(alumnos)

# Cómo agrego items a una tupla... No se puede
# LAS TUPLAS SON INMUTABLES