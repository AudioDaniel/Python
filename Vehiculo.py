from pickle import *

class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Este Vehiculo es de color {} y tiene {} ruedas".format(self.color , self.ruedas )

Toyota = Vehiculo("Rojo",4)
print(Toyota)


f = open('vehiculoDB','w+b')
dump(Toyota, f)

f.seek(0)
ToyotaGuardado = load(f)
print(ToyotaGuardado)
f.close()

"""
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, 
haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
"""