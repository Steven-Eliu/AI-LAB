import csv

datos = [['Usuario', 'Contraseña'],
         ['Alberto', 'Remgio'],
         ['Angel', 'Corrales'],
         ['Arali', 'Mata']]

archivo = open('Base.csv', 'w')
with archivo:
    #Escribir en el archvio
    escritor = csv.writer(archivo)
    escritor.writerows(datos)
