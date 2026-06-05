
# Objetivo: Mostrar el uso de compresión de listas en Python

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doble =[] #lista vacía

for n in numeros:
    doble.append(n*2)

print(doble)

# Genera otra lista de los cuadrados de los números en la lista numeros
cuadrados = [num ** 2 for num in numeros]

lista_cuadruple=list(map(lambda x: x * 4, numeros))
print(lista_cuadruple)

# Genera otra lista con el cubo de cada uno de los numeros de la lista
cubo = [elemento ** 3 for elemento in numeros]

cadena = ["hola "+"que hace" for _ in range(3)]

# Genera una lista de cadenas para cada elemento del rango de 5
saludos = ["hola" for _ in range(5)] #range(0, 5)
saludos2 = ["que hace" for _ in range(3)] #range(0, 3)

#Elabora una serie de ejercicios usando compresión de listas para practicar su uso. P

#ejercicio 1: Generar una lista de los números pares del 1 al 20
pares = [n for n in range(1, 21) if n % 2 == 0]

#ejercicio 2: Generar una lista de las primeras 10 potencias de 2
potencias_dos = [2 ** n for n in range(10)]

#ejercicio 3: Generar una lista de las palabras en una frase dada
frase = "La programación funcional es divertida"
palabras = [palabra for palabra in frase.split()]

