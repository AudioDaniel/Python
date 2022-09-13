import time

Hora = time.strftime("%H")
Minuto = time.strftime("%M")


if int(Hora) >= 19:
    print("Se ha terminado tu jornada laboral,puedes irte a casa")
else:
    print("Te quedan {} horas y {} minutos".format(18-int(Hora),60-int(Minuto)))


"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, 
haréis una operación para calcular el tiempo que queda de trabajo.
"""