###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones
###

from os import system
if system("clear") !=0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas")

### Completa aqui
nombre = "Carlos Alberto Tec Mex"
ciudad = "Felipe Carrillo Puerto"
print(f"Hola me llamo: {nombre}")
print(f"Vivo en la ciudad de: {ciudad}" ) 


print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguienes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí 
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


print("--------------")


print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")

### Completa aquí
cadena = "12345"
num_entero = int(cadena)
num_flotante = float(num_entero)

print(num_entero)
print(num_flotante)

print("Convierte el float 3.99 a un entero, ¿Qué ocurre?")
### Completa aquí
print(int(3.99))
print("R = Al convertir un numero flotante a entero usando int la respuesta seria 3 ya que python elimina los decimales y se queda con el entero")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura")
print("Usa f-string para imprimir una presentación")

# ¡Hola! Me llamo tu_nombre y luego tu_edad años, mido tu_altura metros

## Completa aquí
mi_nombre = "Carlos Alberto Tec Mex"
mi_edad = 22
mi_altura = 1.62

print(f"¡Hola! Soy {mi_nombre} tengo {mi_edad} años y mido {mi_altura} metros")


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI(sin asignar una variable)")
print("2. Redondea el numero con round()")
print("3. Haz la división entera entre el numero que te salió y el numero 2")
print("4. El resultado debería ser 1")

redondeo = (round(3.1416))
print("El numero redondeado es", redondeo)
division = redondeo // 2
print("El resultado de la división es:",division)



