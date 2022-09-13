import tkinter
 
ventana = tkinter.Tk() 

radioValue = tkinter.IntVar() 

### Radiobuttons
rdioOne = tkinter.Radiobutton(ventana, text='Opcion 1',variable=radioValue, value=1) 
rdioTwo = tkinter.Radiobutton(ventana, text='Opcion 2',variable=radioValue, value=2) 
rdioThree = tkinter.Radiobutton(ventana, text='Opcion 3',variable=radioValue, value=3)

#### Reset de los RadioButtons
def reset():
    radioValue.set(None)

### Botón de Reset
boton = tkinter.Button(text= "Reset",command=reset)

    
rdioOne.pack(anchor=tkinter.N)
rdioTwo.pack(anchor=tkinter.N)
rdioThree.pack(anchor=tkinter.N)
boton.pack(anchor=tkinter.S)

ventana.mainloop()

"""
Tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado 
y que contenga un botón de reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.
"""