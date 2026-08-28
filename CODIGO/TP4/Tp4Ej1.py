#funcion que recibe base y altura y devuelve el area
def area_rectangulo(base,altura):
    resultado = base * altura
    return resultado

base = int(input("Ingrese la base del rectangulo"))
altura = int(input("Ingrese la altura del rectangulo"))
resultado = area_rectangulo(base,altura)
print("El resultado es: "+ str(resultado))