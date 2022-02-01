'''Buscar dentro de un archivo CSV el nombre
y contraseña.

Al dar aceptar, si el usuario y la contraseña
estan dentro del archivo, el fondo cambia a azul, y 
se muestra un mss indicando aceptado.

De lo contrario, se pondra en color rojo y se muestra un
mss indicando no validos.

    - Si el usuario existe pero la contraseña no es correcta
    se indica en mss
    
    - Si el usuario no existe tambien se indica en el mss
    
El color inicial sera gris. Con el boton reset, el fondo vuelve a su color 
original y los entry se limpan'''

# Se importan las librerias para trabajare 
import csv
from tkinter import *
from tkinter import messagebox as mss

# Se crea la ventana
ventana = Tk()
ventana.geometry('400x300')
ventana.title("Tarea 3")
ventana.config(bg='gray')

# Se define la funcion 
def Auth():
# Leemos la base de datos con  nuestra funcion
    arreglo = []
    with open('Base.csv') as archivo:
        lector = csv.reader(archivo, delimiter = ',', quotechar = ',', quoting = csv.QUOTE_MINIMAL)
# 
        usuario = E1.get()
        contraseña = E2.get()
        status = False
        message = 'No existe el usuario'
        for renglon in lector:
            if(len(renglon)!=0):
                if (renglon[0] != 'Usuario'):
                    arreglo.append(renglon)
                    if (usuario == renglon[0] and contraseña == renglon[1]):
                        ventana.config(bg='blue')
                        status = True
                        message = 'Aceptado'
                        break
                    elif(usuario == renglon[0] and contraseña != renglon[1]):
                        status = False
                        message = 'Contraseña incorrecta'
        if (status == True):
            mss.showinfo(message=message,title = 'success')
            ventana.config(bg='blue')
        else:
            mss.showerror(message=message,title = 'error')
            ventana.config(bg='red')

def Clean():
    E1.delete(0,END)
    E2.delete(0, END)
    ventana.config(bg='grey')

E1 = Entry(ventana)
E1.place(x = 100, y = 45)
L1 = Label(ventana, text = 'Ingrese su usuario: ')
L1.place(x = 100, y = 15)

E2 = Entry(ventana)
E2.place(x=100, y=105)
L2 = Label(ventana, text='Ingrese su contraseña: ')
L2.place(x=100, y=75)

B1 = Button(ventana, text='Aceptar', command=Auth)
B1.place(x=100, y=200)

B2 = Button(ventana, text='Reset', command = Clean)
B2.place(x=200, y=200)

ventana.mainloop()


