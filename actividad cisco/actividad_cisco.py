# Importamos el módulo strerror de la librería 
from os import strerror

# Inicializa 26 contadores para cada letra latina.
# Utilizamos una comprensión de diccionario para crear un diccionario donde cada letra es una clave y el valor es 0.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# Solicitamos al usuario que ingrese el nombre del archivo a analizar.
file_name = input("Ingresa el nombre del archivo a analizar: ")

try:
    # Intentamos abrir el archivo en modo de lectura de texto ("rt").
    file = open(file_name, "rt")

    # Iteramos sobre cada línea del archivo.
    for line in file:
        # Iteramos sobre cada caracter de la línea.
        for char in line:
            # Si el caracter es una letra...
            if char.isalpha():
                # ...lo convertimos a minúscula y actualizamos el contador correspondiente.
                counters[char.lower()] += 1

    # Cerramos el archivo después de leerlo.
    file.close()

    # Mostramos los contadores para cada letra que tenga un valor mayor a 0 (aparece en el archivo).
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)

except IOError as e:
    # En caso de que ocurra un error de E/S, mostramos un mensaje de error con el código de error.
    print("Se produjo un error de E/S: ", strerror(e.errno))
