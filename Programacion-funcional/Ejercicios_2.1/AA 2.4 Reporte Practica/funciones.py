# Ejemplo CALLBACK

def operar (n1, n2, funcion):
    return funcion(n1, n2)
    
def suma(a, b):
    return a + b 

def resta(a, b):# Funcion de primer orden
    return a - b 

resultado = operar(5, 3, suma)  # La función suma actua como callbacj al ejecutarse en operar
print(resultado)

'''
Un callback es una funcion que se pasa a otra funcion como argumento y se espera que sea llamada dentro de esa función
Las funcionesde primer orden son aquellos que no toman otras funciones como argumentos ni devuelven funciones
'''

# EJEMPLO DE FUNCION PRIMERA CLASE

def saludo():
    return "¡Hola!"

mi_variable = saludo() # Ejecutamos la funcion y la asignamos a una variable
print(mi_variable) # Imprimimos la variable

def saludo2():
    return "¡Que tal!"

mi_variable2 = saludo2 #Asignamos la funcion sin parentesis a una variable, pero no ejecutamos
print(mi_variable2) # Para ejecutar la funcion mas tarde, debes usar parentesis 


# EJEMPLO DE FUNCIÓN DE ORDEN SUPERIOR
def elegir_operacion(operacion): # funcion de orden superior
    def multiplicar(x):
        return x * 2
    def dividir(x):
        return x / 2
    
    if operacion == "multiplicar":
        return multiplicar # Retornamos la función sin ejecutarla 
    
    else:
        return dividir
    
doble = elegir_operacion("multiplicar") # Devuelve la funcion multiplicar
print(doble(10))

divide2 = elegir_operacion("dividir") # Devuelve la funcion dividir
print(divide2(10))

'''
Una funcion de orden superior es aquella que puede recibir otras funciones como argumentos o devolver una funcion como resultado
'''

#EJEMPLO FUNCION ANONIMA = LAMBDA

doble = lambda x: x * 2 #Función anónima que recibe un argumento x y devuelve su doble
print(doble(5))

cuadrado = lambda x: x ** 2 #Función anónima que recibe un argumento x y devuelve su cuadrado
print(cuadrado(4))

def cuadrado(x):
    return x ** 2
print(cuadrado(4))

#funcion de orden superior que recibe una función como argumento
def aplicar_funcion(funcion, valor):
    return funcion(valor)#retorna el resultado de aplicar la función al valor dado
resultado = aplicar_funcion(3) #Pasamos una función lambda que calcula el triple de un número
resultado = aplicar_funcion(lambda x: x ** 3, 3) #Pasamos una función lambda que calcula el cubo de un número
print(resultado)  # Imprime 27, que es el cubo de 3


numeros = [1, 2, 3, 4] #Lista de números
dobles = list(map(lambda x: x * 2, numeros)) #Usamos map para aplicar la función lambda a cada elemento de la lista numeros y obtenemos una nueva lista con los


# Usamos map con la función saludar
#lista_saludos = list(map(saludar, alumnos))
#print(lista_saludos)


'''
Una función anónima, también conocida como función lambda, es una función sin nombre que se define utilizando la palabra clave lambda. Se utiliza para crear funciones pequeñas y de una sola expresión de manera concisa.

Pueden pasarse como argumentos sin necesidad de definirlas antes

Se utilizan cuando la función es simple y solo se necesita en un lugar
'''