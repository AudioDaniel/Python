class Vehiculo():
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self,color,ruedas,puertas,cilindrada,velocidad):
        self.color = color
        self.ruedas = ruedas 
        self.puertas = puertas
        self.cilindrada = cilindrada
        self.velocidad = velocidad 
    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} puertas, {} cilindrada".format( self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )

Toyota = Coche("Rojo",4,4,300,120)
print(Toyota)
