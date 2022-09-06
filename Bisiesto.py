
def calc_anyo_bisiesto(anyo):
    if anyo % 4 == 0 and anyo % 400 !=0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")


calc_anyo_bisiesto(2016)