
# Ejemplos de librerias
# Kivy, qt, tkinter,  pygame

from tkinter import *
from tkinter import messagebox as mss
from turtle import color

# Nombrar la ventana
ventana = Tk()

# Cambiar el tamaño de la venta
ventana.geometry('400x300')
ventana.title('Mi programa')
# ventana.config(Cambiar de color la ventana)
# ventana.iconbitmap(Coloar un icono a nuestra ventana)

def Val():
    resp = mss.askyesno(message='Desea continuar?', title='Continuar')
    if (resp == True):

        T = E1.get() # Obtiene los caracteres del E1
        try:
            x = float(T)
            mss.showinfo(message='Conversion realizada', title='Informacion ')
            E1.delete(0, END)
            # print('Es un numero')
        except:
            mss.showerror(message='Dato incorrecto', title='Error')
            E1.delete(0, END)
            # print('Valor incorrecto')
        # print('Se presiono el boton')

def cambio():
    T = Sp1.get()
    if (T == 'black' or T == 'blue'):
        L1.config(fg='white')
    else:
        L1.config(fg='black')
        
    ventana.config(bg = T)
    L1.config(bg=T)

# Entrada de datos
E1 = Entry(ventana)
E1.place(x = 10, y = 25)
# E1.pack() Coloca el objeto en un lugar al azar 
# E1.grid() Divide la ventana en reng. y column
# E1.place() Coloca el objeto segun 'x' y 'y'

L1 = Label(ventana, text = 'Ingresa un numero: ')
L1.place(x = 10, y = 2)
# L1.config(bg= 'color')

B1 = Button(ventana, text = 'Validar', command=Val)
B1.place(x = 10, y = 50)

colores = ['red', 'black', 'blue', 'white', 'pink', 'gray']
Sp1 = Spinbox(ventana, values=colores, command=cambio)
Sp1.place(x=10, y=75)

ventana.mainloop()

