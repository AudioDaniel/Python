from functools import *

lista = [1,2,3,4,5,6,7,8,9,10]

def calc_pares(a):
    if a % 2 == 0:
        return True
    else: return False

pares = filter(calc_pares,lista)
pares_listificado =list(pares)

def suma(b,c):
    return b + c

pares_sumados = reduce(suma,pares_listificado)

print(pares_listificado)
print(pares_sumados)

"""
Tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y 
realizará una suma de todos estos elementos obtenidos mediante reduce.
"""