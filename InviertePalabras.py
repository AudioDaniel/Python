def invierte_palabras(palabra):
    palabra = palabra.lower()
    longitud=len(palabra)
    palabra_invertida=palabra[longitud::-1]
    print(palabra_invertida)

invierte_palabras("Never Odd or Even")