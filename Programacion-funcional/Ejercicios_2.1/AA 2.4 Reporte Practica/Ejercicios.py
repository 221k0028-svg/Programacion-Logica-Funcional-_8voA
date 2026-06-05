
# EJERCICIO 1 - Inflar globo

print ("EJERCICIO 1 - INFLAR GLOBO")

# 1. Función tradicional que devuelve el emoji de globo
def inflar_globo():
    return "🎈"


# 2. Misma función usando lambda
inflar_globo_lambda = lambda: "🎈"


# 3. Función que prepara los globos según número de invitados
def preparar_globos(numero_invitados):
    # Comprensión de listas llamando a inflar_globo()
    return [inflar_globo() for _ in range(numero_invitados)]


# 4. Solicitar número de invitados al usuario
numero = int(input("¿Cuántos invitados van a la fiesta? "))

# También podemos crear la lista directamente con lambda y comprensión
globos_con_lambda = [inflar_globo_lambda() for _ in range(numero)]

# Usando la función preparar_globos
globos_fiesta = preparar_globos(numero)

# 5. Mostrar resultado
print(globos_fiesta)



# EJERCICIO 2 - Mostrar Menu Cafeteria 

print ("EJERCICIO 2 - MOSTRAR MENU CAFETERIA")

# 1. Función que formatea el menú
def ver_menu(menu):
    # 2 y 3. Comprensión de listas con formato
    return [f"{nombre.capitalize()}: ${precio:.2f}" for nombre, precio in menu.items()]


# 5. Diccionario con el menú
menu = {
    "americano": 25.50,
    "café de olla": 22.00,
    "capuchino": 35.75,
    "coca": 40.00,
    "agua": 18.50
}

# 6. Llamar a la función y guardar resultado
menu_formateado = ver_menu(menu)

# 7. Imprimir cada elemento en una línea separada
for bebida in menu_formateado:
    print(bebida)



# EJERCICIOS 3 - Cuenta de cafeteria 

print ("EJERCICIO 3 - CUENTA CAFETERIA")

from functools import reduce

# Lista de precios de las órdenes
orden = [25.50, 22.00, 35.75, 40.00, 18.50]

print("Precios originales:", orden)

# --- map(): Aplicar 10% de descuento a cada precio ---
# Multiplicar por 0.90 = quitar el 10%
precios_con_descuento = list(map(lambda precio: precio * 0.90, orden))
print("Precios con 10% de descuento:", precios_con_descuento)

# --- filter(): Filtrar solo bebidas caras (más de $25) ---
bebidas_caras = list(filter(lambda precio: precio > 25, precios_con_descuento))
print("Bebidas caras (>$25):", bebidas_caras)

# --- reduce(): Calcular el total a pagar ---
total = reduce(lambda acumulado, precio: acumulado + precio, bebidas_caras)
print(f"Total a pagar: ${total:.2f}")
