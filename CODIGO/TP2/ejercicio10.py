#programa que arma una clave con nombre,apellido y año de nacimiento
#datos de entrada
nombre = input("\nIngrese su nombre: ")
apellido = input("\nIngrese su apellido: ")
anio = input("\nIngrese su año de nacimiento: ")

#se cuentan los caracteres de las variables y se guardan en variables
nombre_cant = len(nombre)
ape_cant = len(apellido)
anio_cant = len(anio)

clave = nombre[nombre_cant -1]+apellido[0]+anio[anio_cant - 1]

print("Clave: " + clave)