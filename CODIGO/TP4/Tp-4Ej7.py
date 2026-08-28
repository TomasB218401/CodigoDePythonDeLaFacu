#funcion que comprueba si un numero es par
def es_par(numero):
    par = (numero % 2 == 0)
    return par

print(es_par(4))
print(es_par(7))
