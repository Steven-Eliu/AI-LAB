#Este es el editor

import csv
from os import lseek
import random

arreglo = []
with open ('ejemplo.csv') as archivo:
    lector = csv.reader(archivo,delimiter = ',', quotechar = ',', quoting = csv.QUOTE_MINIMAL)
    for renglon in lector:
        if (len(renglon) !=0):
            arreglo.append(renglon)

print(arreglo)

#Agregar un valor aleatorio dentro de nuestro arreglo
arreglo2 = []
for i in range (len(arreglo)):
    edad = random.randint(20,35)
    if (i == 0):
        arreglo2.append(['Nombre', 'Apellido', 'Grado', 'Edad'])
    else:
        arreglo[i].append(edad)
        ls = arreglo[i]
        arreglo2.append(ls)

print(arreglo2)    

