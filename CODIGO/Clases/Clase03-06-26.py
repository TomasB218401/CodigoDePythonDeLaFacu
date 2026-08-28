#TAD
class Persona():
    def __init__(self):#metodo constructor
        self.dni = 0
        self.nombre = ""
        self.apellido = ""
        
    def agregar_datos(self,d,n,a):
        self.dni = d
        self.nombre = n
        self.apellido = a


mi_persona = Persona()
nombre = input("Ingrese nombre:")
apellido = input("Ingrese apellido: ")
dni = int(input("Ingrese dni: "))
mi_persona.agregar_datos(dni,nombre,apellido)

        