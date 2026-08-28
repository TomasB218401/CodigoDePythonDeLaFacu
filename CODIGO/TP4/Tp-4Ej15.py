#guarda info de deportes(nombre,año de creacion,
# elemento usado , cantidad de jugadores, puntaje maximo,
# puntaje minimo, reglamento) funcion que procese esto

def procesar_deportes():
    lista = []
    nombre = input("Ingrese el nombre del deporte a registrar: ")
    anio_crea = int(input("Ingrese la fecha en la que se creo : "))
    elemento_usado = input("Ingrese el elemento con el cual se practica el deporte: ")
    cant_jugadores = int(input("Ingrese la cantidad de jugadores: "))
    punt_maximo = int(input("Ingrese el puntaje maximo: "))
    punt_minimo = int(input("Ingrese el puntaje minimo: "))
    reglamento = input("Ingrese el reglamento: ")
    deporte = [nombre,anio_crea,elemento_usado,cant_jugadores,punt_maximo,punt_minimo,reglamento]
    lista = [deporte]
    return lista

def deporte_nombre(deporte,nombre):
    esigual = deporte[0][0] == nombre
    return esigual

def deporte_masCincuenta(deporte):
    comparador = (2026 - deporte[0][1] ) > 50
    return comparador

def multi2_deporte(deporte):
    comparador = deporte[0][1] % 2 == 0
    return comparador

def tiene_eseElemento(deporte,elemento):
    comparador = deporte[0][2] == elemento
    return comparador

def menos_cant_deporte(deporte,numero):
    comparador = deporte[0][3] < numero
    return comparador

def diferencia_puntos(deporte):
    comparador = (deporte[0][4] - deporte[0][5])
    return comparador

def cant_reglamento(deporte):
    cantidad = len(deporte[0][6])
    return cantidad
def empiezaEnvocal(deporte):
    palabra = deporte[0][6]
    resultado = (palabra[0] == "A" or palabra[0] == "a" or palabra[0] == "E" or palabra[0] == "e" or palabra[0] == "I" or palabra[0] == "i" or palabra[0] == "O" or palabra[0] == "o" or palabra[0] == "U" or palabra[0] == "u")  
    return resultado

def terminaEnvocal(deporte):
    palabra = deporte[0][0]
    resultado = (palabra[-1] == "A" or palabra[-1] == "a" or palabra[-1] == "E" or palabra[-1] == "e" or palabra[-1] == "I" or palabra[-1] == "i" or palabra[-1] == "O" or palabra[-1] == "o" or palabra[-1] == "U" or palabra[-1] == "u")
    return resultado

def comienzaConsonante(deporte):
    palabra = deporte[0][6]
    resultado = (palabra[0] != "A" or palabra[0] != "a" or palabra[0] != "E" or palabra[0] != "e" or palabra[0] != "I" or palabra[0] != "i" or palabra[0] != "O" or palabra[0] != "o" or palabra[0] != "U" or palabra[0] != "u")
    return resultado

def hace_cuanto_se_creo(deporte):
    anio = deporte[0][1]
    resultado = 2026 - anio
    return resultado

def ver_deporte(deporte):
    nombre = deporte[0][0]
    cantj = deporte[0][3]
    elem = deporte[0][2]
    pmax = deporte[0][4]
    pmin = deporte[0][5]
    anio = deporte[0][1]
    reglamento = deporte[0][6]
    return print(f" Nombre deporte: {nombre} \n Cantidad de Jugadores: {cantj} \n Elemento: {elem} \n Puntaje Max: {pmax} \n Puntaje Min: {pmin} \n Creado: {anio} \n Reglamento: {reglamento}")
    
lista_dep = procesar_deportes()
resultado = diferencia_puntos(lista_dep)
res = cant_reglamento(lista_dep)
sss = empiezaEnvocal(lista_dep)
op = terminaEnvocal(lista_dep)
consonante = comienzaConsonante(lista_dep)
cuanto = hace_cuanto_se_creo(lista_dep)
ver_deporte(lista_dep)

    
    
    