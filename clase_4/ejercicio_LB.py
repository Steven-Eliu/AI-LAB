''' Crear una interfaz donde el usuario pueda ingresar 
sus datos (Altura, peso, no pie) y al hacer la funcion bayesiana 
le calcule a que grupo pertenece

/// Si uno o mas de los entry esta vacio, desplegar un messagebox
/// Si los Entry se tienen letras arrojar un messabox error. y resetear los entry
/// En la respuesta aparece la clase a la que corresponde (Hombre o mujer)'''

# Se importan las librerias para trabajar
import csv
from tkinter import *
from tkinter import messagebox as mss
from turtle import position

# Se crea la ventana
ventana = Tk()
ventana.geometry('400x300')
ventana.title("Bayesiano")



ventana.mainloop()
