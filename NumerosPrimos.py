def calc_numeros_primos(numero):
    if numero > 1:
        for n in range(2,numero):
            if numero % n ==0:
                print("No es primo", n, "es divisor")
                return False
    print("Es primo")
    return True


calc_numeros_primos(13)