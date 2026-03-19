##

from os import system
if system("clear") !=0: system("cls")

# Para obtener datos del usuario se usa la funcion input()
#
nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

# Ten en cuenta que la funcion input() devuelva un string
# Asi que si queremos obtener un numero se debe convertir el string a un numero

age = input("¿Cuantos años tiene? \n")
age = int(age)
print(f"Tienes {age} años")

# La funcion input() tambien puede devolver multiples valores
# Para hacerlo, el usario debe separar los valores con una coma
print("Obtener multiples valores a la vez")
country, city = input("¿En que pais y ciudad vives? \n").split() #.split "separa"

print(f"vives en {country}, {city}")