def comparar_longitud(a1,a2):
    x = len(a1)
    y = len(a2)
    #comparo
    ok = (x == y)
    return ok
def concatenar_listas(a1,a2):
    a3 = a1+a2
    return a3
def terminan_igual_elemento(a1,a2):
    ulta1 = a1[len(a1)-1]
    ulta2 = a2[len(a2)-1]
    ok = (ulta1 == ulta2)
    return ok

def menos_elementos(a1,nro):
    x = len(a1)
    y = x < nro
    return y

#programa principal
#invocamos las fucniones
nro = int(input("Ingrese un nro: "))
palabra = input("Ingrese una palabra: ")
lista1 = [nro,palabra]
lista2 = []
lista2.append(palabra)
lista2.append(nro)
lista3 = concatenar_listas(lista1,lista2)
son_iguales = comparar_longitud(lista1,lista2)
print(son_iguales)
son_iguales2 = terminan_igual_elemento(lista1,lista2)
print(son_iguales2)

menosEL = menos_elementos(lista3,nro)

