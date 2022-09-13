class Alumno():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def checknota(self):
        print("Tienes un " + str(self.nota) + " estas: ")
        if self.nota < 5:
            print("Suspenso")
        else: print("Aprobado")

Jose = Alumno
Laura = Alumno

Jose.__init__(Jose,Jose,3)
Laura.__init__(Laura,Laura,8)

## Imprimimos los resultados

Laura.checknota(Laura)


### En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y 
# mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
###