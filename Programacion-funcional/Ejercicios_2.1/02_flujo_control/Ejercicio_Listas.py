###
# EJERCICIOS DE LISTAS
###

from os import system
if system("clear") !=0: system("cls")

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print("\n Ejercicio 1: El mensaje secreto")
print("Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje secreto")

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

secreto = mensaje[7:14]
print(secreto)

print("------------------------------------")

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("\n Ejercicio 2: Intercambio de posiciones")
print("Intercambia la primera y la última posición utilizando solo asignación por índice")

numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[4] = numeros[4], numeros[0]

print(numeros)

print("------------------------------------")

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

print("\n Ejercicio 3: sándwich de listas")
print("Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden")

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo

print(sandwich)


print("------------------------------------")

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

print("\n Ejercicio 4: Duplicando la lista")
print("Crea una nueva lista que contenga los elementos de la lista original duplicados")

lista = [1, 2, 3]

duplicada = lista + lista

print(duplicada)

print("------------------------------------")

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("\n Ejercicio 5: Extrayendo el centro")
print("Extrae el elemento que se encuentra en el centro de la lista utilizando slicing.")

lista = [10, 20, 30, 40, 50]
centro = lista[2:3]

print("Centro (como lista):", centro)
print("Centro (valor):", centro[0])

print("------------------------------------")

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
# Ejercicio 6: Reversa parcial

print("\n Ejercicio 6: Reversa parcial")
print("Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación")

lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2

# Invertir la primera mitad
primera_parte = lista[:mitad][::-1]
# Segunda mitad sin cambios
segunda_parte = lista[mitad:]
# Unir ambas partes
resultado = primera_parte + segunda_parte

print(resultado)