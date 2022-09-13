import tkinter

ventana = tkinter.Tk()

lista = ('Spain','Portugal','Francia')
var= tkinter.Variable(value=lista)

listbox1 = tkinter.Listbox(
    ventana,
    listvariable=var,
    height=4,
    selectmode=tkinter.EXTENDED)

etiqueta = tkinter.Label(ventana,text="Paises")


etiqueta.pack(anchor=tkinter.N)
listbox1.pack(anchor=tkinter.N)
ventana.mainloop()
"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener 
una lista de elementos seleccionables, 
también debe de tener un label con el texto que queráis.

"""