#sabemos la cantidad de repeticiones
#el programa verifica cuales letras son vocales y cuales consonantes
conjunto = input("Ingrese una frase: ")
lista_vocal = []
lista_cons = []
lista_espacios = []
lista_puntos = []
vocales = "a","e","i","o","u"
for x in conjunto:
    print(x)
    if x in vocales:
        lista_vocal.append(x)
    elif(x == " "):
        lista_espacios.append(x)
    elif(x == "."):
        lista_puntos.append(x)
    else:
        lista_cons.append(x)
