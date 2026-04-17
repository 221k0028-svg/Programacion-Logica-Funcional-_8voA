###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

print("\nEjercicio 1: Cuenta atrás")

numero = 10
while numero >= 1:
    print(numero)
    numero -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

print("\nEjercicio 2: Suma de números pares")

numero = 1
suma = 0

while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1

print(f"La suma de los números pares es: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número.
# Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

print("\nEjercicio 3: Factorial")

numero = -1

while numero < 0:
    numero = int(input("Escribe un número entero positivo: "))
    if numero < 0:
        print("Debe ser positivo")

factorial = 1
contador = numero

while contador > 0:
    factorial *= contador
    contador -= 1

print(f"El factorial de {numero} es {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

print("\nEjercicio 4: Validación de contraseña")

contrasena = ""

while len(contrasena) < 8:
    contrasena = input("Introduce una contraseña (mínimo 8 caracteres): ")
    if len(contrasena) < 8:
        print("La contraseña es muy corta")

print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

print("\nEjercicio 5: Tabla de multiplicar")

numero = int(input("Introduce un número: "))
contador = 1

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

print("\nEjercicio 6: Números primos")

n = int(input("Introduce un número: "))
numero = 2

while numero <= n:
    divisor = 1
    contador_divisores = 0

    while divisor <= numero:
        if numero % divisor == 0:
            contador_divisores += 1
        divisor += 1

    if contador_divisores == 2:
        print(numero)

    numero += 1