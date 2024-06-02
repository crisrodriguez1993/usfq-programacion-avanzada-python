# Importar modulos/paquetes
# from funciones import *
# import funciones

from funciones import *
# import funciones // tengo que usar funciones.funcion()

if __name__ == "__main__":
    saludar()
    imprimirNombre([0])
    describir_animal("Perro", "Firulais")
    describir_animal(nombre_animal="Jack", tipo_animal="Perro") # keyword argument
    describir_animal2("Pelusa")

    valores = [10000, 56.76, 30000, 3000, 200]
    prom = promedio(valores)
    print(prom)

    imprimir_nombre_formato("Ramiro", "Sandoval")
    imprimir_nombre_formato("Michael", "Fox", "J.")

    hacer_pizza("Queso", "Salsa", "Pepperoni", "Jamon")

    hacer_pizza2("Mediana", "Queso", "Salsa", "Tocino")

    hacer_pizza3(tamanio="Grande", queso="Extra")

    perfil = construir_perfil("Albert", "Einstein", 
                              ubicacion="Princeton", campo="Fisica")
    print(perfil)

    hacer_pedido("Taco", 'Queso', 'Carne', "Frejol", tiempo_entrega="inmediato")

    contador = contador_infinito()

    for _ in range(10):
        print(next(contador))
    
    for _ in range(10):
        print(next(contador))

    for _ in range(20):
        try: # intente hacer esto
            print(next(contador))
        except StopIteration:
            # si hay una excepcion del tipo StopIteration
            pass # no haga nada

    '''for temperatura in generador_temperaturas(25):
        print(temperatura)'''

    temp = generador_temperaturas2()
    for _ in range(20):
        print(next(temp))

