###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

print("\nEjercicio 1: Números pares")

for numero in range(2, 21):
    if numero % 2 == 0:
        print(numero)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

print("\nEjercicio 2: Media de una lista")

numeros = [10, 20, 30, 40, 50]
suma = 0

for numero in numeros:
    suma += numero

media = suma / len(numeros)

print(f"La media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

print("\nEjercicio 3: Número máximo")

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]

for numero in numeros:
    if numero > maximo:
        maximo = numero

print(f"El número máximo es: {maximo}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

print("\nEjercicio 4: Filtrar palabras")

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

# usando for normal
resultado = []

for palabra in palabras:
    if len(palabra) > 5:
        resultado.append(palabra)

print(resultado)

# usando list comprehension
resultado2 = [palabra for palabra in palabras if len(palabra) > 5]
print(resultado2)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

print("\nEjercicio 5: Contar palabras por letra")

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

letra = input("Introduce una letra: ").lower()
contador = 0

for palabra in palabras:
    if palabra.lower().startswith(letra):
        contador += 1

print(f"Cantidad de palabras que empiezan con '{letra}': {contador}")