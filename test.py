# start=1
# end=5

def squares(start,end):
    lista = []
    for x in range(start,end+1):
        lista.append((pow(x,2)))
    return lista

print(squares(1,5))

