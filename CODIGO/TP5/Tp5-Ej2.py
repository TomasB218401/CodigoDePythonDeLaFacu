#definir funcion que retorna tupla con colores primarios
#definir una funcion que recibe el nombre de color, la funcion devuelve true o false si el color
#es un color primario
#escribir programa que determina si un color es primario o no

#funciones

def ColoresPrim():
    Colores = ("rojo","amarillo","azul")
    return Colores

def seraPrimario(color,tupla):
    if (color in tupla):
        return print("Es un color primario")
    else:
        return print("No es color primario")
def ProcesarColor():
    color = input("Ingrese un color: ")
    return color

#Programa principal
Color = ProcesarColor()

seraPrimario(Color,ColoresPrim())
