def Procesar_Empleados():
#procesar datos de 3 empleados
    lista_em = []
    for n in range(3):
        nombre = input("Ingrese Nombre: ")
        apellido = input("Ingrese Apellido: ")
        cargo = input("Ingrese Cargo: ")
        empleado = [nombre,apellido,cargo]
        lista_em.append(empleado)
    return lista_em

#el [][] el primero sirve para buscar el conjunto y el segundo el
#El elemento especifico de ese conjunto
#print(lista_em[1][1])
#Definir una funcion que recibe como parametro una lista de empleados
#y agrega en la lista el año de antiguedad a cada empleado
def agregar_antiguedad(lista):
    nueva = []
    for empleado in lista:
        antiguedad = int(input("Ingrese la antiguedad: "))
        empleado.append(antiguedad)
        nueva.append(empleado)
    return nueva
#definir funcion que tome datos de una lista de empleados y devuelva
#las inciciales de cada uno

def iniciales_empleados(lista):
    ini_emp = []
    for empleado in lista:
        x = empleado[0][0]
        y = empleado[1][0]
        z = x,y
        ini_emp.append(z)
    return ini_emp

def imprimir_iniciales(lista):
    print("Iniciales")
    for i in lista:
        print("Nombre: "+i[0]+"\n"+"Apellido: "+i[1])

    


empleados = Procesar_Empleados()
empleados = agregar_antiguedad(empleados)
iniciales = iniciales_empleados(empleados)
print(iniciales)
imprimir_iniciales(iniciales)