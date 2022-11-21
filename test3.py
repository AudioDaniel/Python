def invierte_palabras(palabra):
    palabra = palabra.lower()
    longitud=len(palabra)
    palabra_invertida=palabra[longitud::-1]
    return(palabra_invertida)
def is_palindrome(input_string):
    palabralower = input_string.lower()
    palabrainversa = invierte_palabras(input_string)
    if palabrainversa == palabralower:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True