#Crea un diccionario llamado persona con la siguiente información
#nombre "Julieta" Edad 19 Ciudad "Quilmes" despues imprimir en pantalla
Persona = {
    "Nombre": "Julieta",
    "Edad" : 19,
    "Ciudad" : "Quilmes"
}
print("Nombre: " + Persona["Nombre"] +"\n"+ "Edad: " + str(Persona["Edad"]) + "\n" + "Ciudad: " +Persona["Ciudad"])

#Modificar la edad de persona a 21 e imprimirla en pantalla
Persona["Edad"] = 21
print(Persona["Edad"])
#Añadir una nueva clave (Profesion con el valor Ingeniero) y eliminar ciudad
#Imprimir el diccionario

#agregar o modificar valor
Persona["Profesion"] = ["Ingeniero"]
print(Persona)
#Eliminar valor
del(Persona["Ciudad"])

print(Persona)



