#Pedir el cuit que tiene la siguiente
#forma xx/dni/x. Extraer y mostrar el dni.

#cuit = input("Ingrese su cuit: ")
#dni = cuit[2:len(cuit)-1]

#print("Su DNI es: "+ str(dni))

#Mostrar el código ASCII de los caracteres “@”, “á” y “¿”
codigoA1 = "EL codigo ASCII de @ es: " + str(ord("@"))
codigoA2 = "EL codigo ASCII de á es: " + str(ord("á"))
codigoA3 = "EL codigo ASCII de ¿ es: " + str(ord("¿"))

print(codigoA1 + "\n" + codigoA2 + "\n" + codigoA3)

# Pedir la cuenta de mail al usuario y mostrar por separado su usuario y su dominio.
mail = input("Ingrese su cuenta de mail : ")
#discrimina una cadena de caracteres, la corta y la pone en una lista
#separada por el discriminante en este caso "@"
Persona = mail.split("@")
Usuario = Persona[0]
dominio = Persona[1]

print("Su Usuario es: "+ str(Usuario))
print("Su Dominio es: "+ str(dominio))