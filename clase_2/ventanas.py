from tkinter import messagebox as ms

#showinfo()
#showwarning()
#showerror()

#askquestion()
#askyesno()
#askokcancel()
#askoknocancel()

#/n salto de linea 


#ms.showinfo(message='Esto es una prueba de informacion', title='ventana')
#ms.showerror(message='Esto es una /n prueba de informacion', title='ventana')
#ms.showwarning(message='Esto es una prueba de informacion', title='ventana')


valor = ms.askokcancel(message='Desea continuar', title= 'Pregunta')
print(valor)

valor = ms.askyesno(message='Desea continuiar', title='pregunta')
print(valor)