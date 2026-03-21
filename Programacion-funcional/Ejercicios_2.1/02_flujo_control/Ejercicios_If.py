##
#EJERCICIOS IF
##

from os import system
if system("clear") !=0: system("cls")

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\n Ejercicio 1: Determinar el mayor de dos números")
print("Pide al usuario que introduzca dos números y muestra un mensaje de cual es mayor o si son iguales")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 > num2:
    print("El primer numero es mayor")
elif num2 > num1:
    print("El segundo numero es mayor")
else:
    print("Los numeros son iguales")



print("------------------------------------")



# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre cero)

print("\n Ejercicio 2: Calculadora simple")
print("Pide al usuario dos números y una operación (+, -, *, /) y realiza la operacion")

numero1 = float(input("Ingrese un numero"))
numero2 = float(input("Ingrese otro numero"))
operaciones = input("Que operacion desea realizar (+, -, *, /)")

if operaciones == "+":
    resultado = numero1 + numero2
    print("El resultado es: ", resultado)

elif operaciones =="-":
    resultado = numero1 - numero2
    print("El resultado es: ", resultado)

elif operaciones == "*":
    resultado = numero1 * numero2
    print("El resultado es: ", resultado)

elif operaciones == "/":
    if numero2 == 0:
        print("No se puede dividir entre 0")
    else:
        resultado = numero1 / numero2
        print("El resultado es: ", resultado)



print("------------------------------------")



# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\n Ejercicio 3: Año bisiesto")
print("Pide al usuario que introduzca un año y determina si es bisiesto.")

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Si es un año bisiesto")
else:
    print("No es un año bisiesto")



print("------------------------------------")



# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0–2 años)
# - Niño (3–12 años)
# - Adolescente (13–17 años)
# - Adulto (18–64 años)
# - Adulto mayor (65 años o más)

print("\n Ejercicio 4: Categorizar edades")
print("Pide al usuario dos números una operación edad y la clasifique en Bebe, Niño, Adolescente, Adulto, Adulto mayor")

edad = int(input("Introduzca una edad: "))

if edad <= 2 :
    print(" Es bebe ")
elif edad <= 12:
    print("Es un niño")
elif edad <= 17:
    print("Es un adolecente")
elif edad <= 64:
    print("Eres un adulto")
else:
    print("Es un adulto mayor")
