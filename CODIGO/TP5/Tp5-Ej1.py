#funcion que procesa notas del alumno
def Procesar_notas():
    lista = []
    nota1 = int(input("Ingrese su primera Nota: "))
    nota2 = int(input("Ingrese su seunda Nota: "))
    notas = [nota1,nota2]
    lista.append(notas)
    return lista

def Nota_mayor(notas):
    n1 = notas[0][0]
    n2 = notas[0][1]
    if(n1 > n2):
        return n1
    elif(n2 > n1):
        return n2
    else:
       return "las notas son iguales"

def Promedio(notas):
    n1 = notas[0][0]
    n2 = notas[0][1]
    prom = (n1 + n2)/2
    return prom


lista = Procesar_notas()

Mayor = Nota_mayor(lista)
print(f"La nota mayor es: {Mayor}")
Promedio = Promedio(lista)
print(f"El Promedio de las notas es: {Promedio}")


