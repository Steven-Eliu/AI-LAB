import csv

datos = [['Clase', 'Altura', 'Peso', 'No de pie' ]]

ingresar = input('Desea ingresar datos? Y / N: ')
while (ingresar == 'Y') :
    x = []
    Clase = input('Ingrese H o M: ')
    Altura = input('Ingrese altura en CM, (ejem: 170): ')
    Peso = input('Ingrese el peso en KG:')
    No_pie = input('Ingrese el No de calzado: ')
    # Asegurar que no se ingresen datos vacios
    if ((len(Clase) > 0) and (len(Altura) > 0) and (len(Peso) > 0) and (len(No_pie) > 0)):
        x.append(Clase)
        x.append(Altura)
        x.append(Peso)
        x.append(No_pie)
        datos.append(x)
    else:
        print('Datos incorrectos, vuelve a ingresar valores')
    ingresar = input('Desea ingresar datos? Y / N: ')

archivo = open('db.csv', 'w')
with archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

print('Escritura exitosa')

# Se creo la base de datos de nuestro proximo algoritmo
