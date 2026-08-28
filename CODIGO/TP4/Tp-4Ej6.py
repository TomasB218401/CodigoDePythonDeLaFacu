#Definir una función clave, que recibe 3 datos como parámetro
#(fecha, dni, apellido), la función
#deberá devolver/retornar la clave conformada por:
# fecha:23/09/2002 dni 12345678 apellido perez Minimo 2 letras
#clave 0918_EZ

#funcion que procesa una persona

def procesar_persona():
    Fecha = input("Ingrese la fecha de su nacimiento con el siguiente formato dd/mm/aaaa: ")
    Dni = input("Ingrese su dni de 8 digitos: ")
    Apellido = input("Ingese su apellido: ")
    Persona = [Fecha,Dni,Apellido]
    return Persona

def funcion_clave(persona):
    fecha = str(persona[0][3:5])
    dni = str(persona[1][0]) + str(persona[1][-1])
    ape = "_"+str(persona[2][-2:]).upper()
    clave = fecha + dni + ape
    return clave

persona_creada = procesar_persona()

clave = funcion_clave(persona_creada)

print(clave)

