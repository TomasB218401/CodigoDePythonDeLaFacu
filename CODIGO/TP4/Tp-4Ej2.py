#Programa que dice true o false si la variable texto tiene vocales
def tiene_vocales(texto):
    tiene_vocal = "a" in texto or "e" in texto or "i" in texto or "o" in texto
    return tiene_vocal

textito = "albin"
print(tiene_vocales(textito))

# Definir una función contiene_palabra(texto, palabra)
#que devuelva True si la palabra está en el
#texto, False si no

def contiene_palabra(texto,palabra):
    palabra_en_texto = palabra in texto
    return palabra_en_texto

palabra = "lopoldo"
texto = "tiene una lopoldo casa"
resultado = contiene_palabra(texto,palabra)

print(resultado)


