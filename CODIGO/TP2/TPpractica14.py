#Escribe un programa que pide tres palabras al usuario y júntalas en una sola
#oración.
palabra1 = input("Escriba la primera palabra: ")
palabra2 = input("Escriba la segunda palabra: ")
palabra3 = input("Escriba la tercera palabra: ")

lista_Palabras = [palabra1,palabra2,palabra3]

nueva_Oracion = " ".join(lista_Palabras)

print(nueva_Oracion)