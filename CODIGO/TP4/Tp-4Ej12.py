#def func recibe una palabra la funcion devuelve true
#o false si la palabra se palindroma

def espali (palabra):
    newpalabra = palabra[::-1]
    resultado = palabra == newpalabra
    return resultado

palabra = "radar"

resu = espali(palabra)

print(resu)