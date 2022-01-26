#Codigo lector de archicos CSV
import csv

arreglo = []
with open ('ejemplo.csv') as archivo:
    lector = csv.reader(archivo,delimiter = ',', quotechar = ',', quoting = csv.QUOTE_MINIMAL)
    for renglon in lector:
        if (len(renglon) !=0):
            arreglo.append(renglon)

print(arreglo)
