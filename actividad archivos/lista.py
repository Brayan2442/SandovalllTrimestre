from Pais import *
import csv

listapais = []
with open("C:\\pais.csv", encoding='utf-8') as archivo:
    csvReader = csv.reader(archivo)    
    for row in csvReader:
        ob = Pais(row[1], row[15], row[17], row[12])
        listapais.append(ob)

total_fertil = 0
total_densidad = 0
total_eda_ema = 0

with open("resultados.txt", "w", encoding='utf-8') as resultados_file:
    for apr in listapais:
        print('pais:', apr.getPais())
        print('Fertil:', apr.getFertil())
        print('Dencidad:', apr.getDens())
        print('Eda_ema:', apr.getEda_ema())

        # Verificar y sumar valores numéricos
        if apr.getFertil().replace('.', '', 1).isdigit():
            total_fertil += float(apr.getFertil())
        if apr.getDens().replace('.', '', 1).isdigit():
            total_densidad += float(apr.getDens())
        if apr.getEda_ema().replace('.', '', 1).isdigit():
            total_eda_ema += float(apr.getEda_ema())

    # Imprimir y guardar los resultados numéricos
    resultados_file.write(f"Total Fertil: {total_fertil}\n")
    resultados_file.write(f"Total Densidad: {total_densidad}\n")
    resultados_file.write(f"Total Eda_ema: {total_eda_ema}\n")

print("Resultados guardados en resultados.txt")

