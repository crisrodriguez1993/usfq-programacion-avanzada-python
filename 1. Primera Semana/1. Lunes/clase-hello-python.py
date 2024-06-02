
if __name__ == "__main__":
    print("Hola!")

    # Los comentarios de una linea son con el hashtag '#'

    '''
    Esto es un comentario
    multi linea.
    '''

    '''
    En otros lenguajes:
        Variable: es un contenedor que tiene nombre y direccion y almacena un valor.
    Python:
        Variable: es una etiqueta asociada a un valor (nombre -> valor)
    '''
    # Una variable que se llama message y tiene el valor "Hola!"
    # Operador de asignacion (=)
    message = "Hola!"
    print(message) # Va a mostrar "Hola!" en la pantalla

    message = "Chao!"
    print(message)

    '''
    Dar nombre y usar variables:
    1. Los nombres de las variables: contener letras, numeros y guiones bajos.
    Pueden empezar con letras y guiones bajos pero no con numeros
    (ej: mensaje_1 | correcto - 1_mensaje | incorrecto)

    2. No se permite el uso de espacios en blanco dentro del nombre de la variable
    y usualmente se utiliza los guiones bajos para representar espacios
    (ej: mensaje_largo | correcto - mensaje largo | incorrecto)

    3. Evitar usar palabras claves y funciones internas de python como 
    nombres de variables. No crear una variable que se llame print porque 
    puede hacer conflicto con la funcion print().

    4. Nombres de variables deberian ser cortos pero descriptivos.
    Por ejemplo ("nombre" es mejor "n")
    Por ejemplo ("nombre_estudiante" a "n_e")

    5. Tener cuidado con las letras l y las O porque a veces se confunden con los
    numeros 1 y 0.
    '''

    '''
    Tipo de dato: String (cadena una caracteres)
    Cualquiera cosa que este dentro de las doble comillas "",
    o de la comilla simple '' se interpreta como un string
    '''
    nombre = "el profesor se llama 'ramiro sandoval'"
    nombre = 'el profesor se llama "ramiro sandoval"'

    '''
    Cambiar a mayusculas, minusculas o capitalizar
    '''
    print(nombre.title()) # La primera letra de cada palabra mayuscula
    print(nombre.upper()) # Hacer todo el texto en mayusculas
    print(nombre.lower()) # Hacer todo el texto en minisculas

    '''
    La longitud de un texto se obtiene con el metodo len() 
    '''
    print(len(nombre))

    '''
    Usar variables dentro de strings
    string con formato
    se declara colocando la letra f antes del texto ""
    '''

    nombre = "Ramiro"
    apellido = "Sandoval"

    print(f"El nombre del profesor es: {nombre} {apellido}.") # printf
