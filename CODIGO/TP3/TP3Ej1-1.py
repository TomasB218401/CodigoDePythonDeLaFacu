#programa que crea 1 tupla con 5 elementos
#y muestra el tercer elemento
Colores = ("Rojo","Amarillo","Verde","Azul","Violeta")
print(Colores[3-1])

#Dadas dos tuplas unirlas en una tupla nueva

OtrosColores = ("Naranja","Celeste","Magenta","Bordo")
ListaColorCombinada = Colores + OtrosColores

#Escribir un programa que evalue si lo ingresado esta en una tupla

ColorUser = input("Hola, por favor ingrese el nombre de un color para verificar si esta o no en la tupla : ")
Resultado = ColorUser in ListaColorCombinada
print(Resultado)

#Dada una tupla con 3 valores, almacenala en una variable y muestra su contenido

TuplaJuan = ("Juan","Malara",22)
Mensaje1 = "Hola mi nombre es: "+TuplaJuan[0]+" "+TuplaJuan[1]+" Y tengo "+str(TuplaJuan[2])+" Años De edad. "
print(Mensaje1)
