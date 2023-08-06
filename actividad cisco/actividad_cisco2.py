from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
counters['numeric'] = 0
counters['special'] = 0

file_name = input("Ingresa el nombre del archivo a analizar: ")

try:
    with open(file_name, "rt") as file:
        for line in file:
            try:
                for char in line:
                    if char.isalpha():
                        counters[char.lower()] += 1
                    elif char.isdigit():
                        counters['numeric'] += 1
                    else:
                        counters['special'] += 1
            except UnicodeDecodeError:
                print("Error de decodificación Unicode al leer un caracter.")
except FileNotFoundError:
    print("El archivo especificado no se encontró.")
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

for char in counters.keys():
    c = counters[char]
    if c > 0:
        print(char, '->', c)
