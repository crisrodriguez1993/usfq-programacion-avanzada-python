'''
Funciones
- Son bloques de codigo que estan diseñados para cumplir una tarea especifica.
- Tienen nombre y pueden tener o no parametros
- Puedo recibir cualquier tipo de dato y puedo retornar cualquier tipo de dato
e incluso a veces puedo retornar mas de un dato a la vez
- Puede tener o no un return, Si no hay return, 
la funcion retorna un None (NULL) por default 

Syntaxis:

Funcion sin parametros/argumentos
def nombre():
    (codigo que pertenece a la funcion)

Funcion con parametros/argumentos
def nombre(arg1, arg2):
    (codigo que pertenece a la funcion)

'''

# Funcion sin parametros
def saludar():
    print("Hola")

# argumento: tipo_dato (ayuda de que tipo de dato es,
# pero python no te obliga a cumplirlo)
def imprimirNombre(nombre: str):
    '''
    Recibe un nombre y lo imprime en consola
    '''
    print(nombre)

# Argumentos son posicionales
def describir_animal(tipo_animal: str, nombre_animal: str):
    print(f"Tengo un {tipo_animal} que se llama {nombre_animal}")

# Valores por default
# Una vez que especifico el primer argumento con valor default,
# todos los argumentos que vienen a continuacion tienen que tener
# tambien valores default
def describir_animal2(nombre_animal:str, tipo_animal: str = "Perro"):
    print(f"Tengo un {tipo_animal} que se llama {nombre_animal}")

'''
Error: non-default argument follows default argument
def describir_animal2(tipo_animal: str = "Perro", nombre_animal:str):
    print(f"Tengo un {tipo_animal} que se llama {nombre_animal}")
'''

def promedio(datos: list) -> float:
    '''
    Suma todos los elementos de la lista y los divide
    para el numero de elementos

    Retorna el promedio
    '''
    return sum(datos)/len(datos)

'''
Sobrecarga de funciones/metodos
Funciones que tienen el mismo nombre pero se distinguen entre si por el numero
parametros o el tipo de parametros

Python no soporta de manera nativa la sobrecarga de funciones
'''

# Manera criolla de hacer sobrecarga de funciones
def imprimir_nombre_formato(nombre: str, apellido: str, 
                            segundo_nombre: str = None):
    if segundo_nombre is not None:
        print(f"{nombre} {segundo_nombre} {apellido}")
    else:
        print(f"{nombre} {apellido}")

# Recibir un numero arbitrario de parametros
def hacer_pizza(*ingredientes: str) -> None:
    '''
    Todos los parametros separados por coma se almacenan dentro del argumento
    ingredientes como una tupla
    '''
    print(ingredientes)
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")

def hacer_pizza2(tamanio, *ingredientes):
    print(f"Tamaño es: {tamanio}")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")

# Numero arbitrario de argumentos pero con palabras clave
def hacer_pizza3(**kwargs):
    '''**kwargs numero arbitrario de argumentos por clave (diccionario)'''
    print(kwargs)
    print(f"{kwargs['tamanio']}")
    print(f"{kwargs['queso']}")

def construir_perfil(nombre, apellido, **datos_biograficos):
    datos_biograficos['nombre'] = nombre
    datos_biograficos['apellido'] = apellido
    return datos_biograficos

def hacer_pedido(comida, *ingredientes, **consideraciones):
    print(comida)
    print(ingredientes)
    print(consideraciones)

'''
Generador: "Lazy Function" -> Funcion vaga
No genera/ocupa/opera con todos los datos al mismo tiempo
Le da un efecto cuando y como usar los datos
Manejar datos "potencialmente infinitos"

# Ejemplo #1: Voy a poder abrir un archivo gigantesco de manera controlado
# Ejemplo #2: Controlar la lectura / entrada de un sensor o feed datos
'''


'''
return: se termina la ejecucion de la funcion
yield: esta es la porcion que te voy a entregar para esta iteracion
'''

"""
def leer_en_bloques(file_objeto, tamanio_bloque=1024):
    '''
    Cargar unicamente un bloque de 1024 (1k) al mismo tiempo a mi memoria
    enves de cargar X tamaño del archivo completo
    '''
    while True:
        data = file_objeto.read(tamanio_bloque)
        if not data:
            break
        yield data # yield -> ceder el paso
    
# Como abrir archivos en python
with open("archivo_grande.data") as file:
    for parte in leer_en_bloques(file):
        print(parte)
"""

def contador_infinito(stop=35):
    count = 0
    while True:
        if count == stop:
            break
        yield count
        count += 1

import random # random me ayuda a generar valores aleatorios
import time # funciones de tiempo, sleep del programa

# C++ = rand()%10+15 [15,25]
def generador_temperaturas(cantidad):
    for i in range(cantidad):
        time.sleep(1)
        temperatura = 15 + (random.random() * 10)
        yield round(temperatura, 2)

def generador_temperaturas2():
    while True:
        time.sleep(1)
        temperatura = 15 + (random.random() * 10)
        yield round(temperatura, 2)