'''Realizar un programa que valide si un archivo CSV
existe un usuario llamando 'Cañedo' y la contraseña 'Ailab'

En caso de existir enviar el mensaje showinfo ('Bienvenido') 
si se introducen los valores erroneos, indicar con showerror 
datos incorrectos

Generar una base de datos con dos columnas que sean usuario y contraseña 
Poner al menos 3 usuarios con su respectiva contraseña 
y en otro programa pedir nombre y contraseña'''

import csv

from sqlalchemy import false

datos = [['Nombre', 'Contraseña'], ['Cañedo', 'Ailab'], ['Steven', 'Hola'], ['Tita', 'Perra'], ['Pinky', 'Shihuhua']]

archivo = open('base.csv', 'w')
with archivo:
    #Escribir en el archvio
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

valido = false

def validar(valor):
    return False

while not valido:
    valor = [datos['Nombre']]
    valido = validar(valor)

