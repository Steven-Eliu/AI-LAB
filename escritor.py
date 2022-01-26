import csv

datos = [['Nombre', 'Apellido', 'Grado'],
        ['Alberto', 'Remgio', 'Ing. Computacion'],
        ['Angel', 'Corrales', 'Ing.Civil'],
        ['Arali', 'Mata', 'Ing. Mecatronica']]

archivo = open('ejemplo.csv', 'w')
with archivo:
    #Escribir en el archvio
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

print('Escritura exitosa')