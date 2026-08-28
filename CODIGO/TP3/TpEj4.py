#repaso

#n1 = 120 y n2 = "9.10" hacer conversion para sacar la division
#y el resto
n1 = 120
n2 = "9.10"
result1 = n1 // float(n2)

result2 = n1 % float(n2)
print("Division entera: "+ str(result1))

print("Resto : "+ str(result2))

#Pedir 5 palabras y devolver la cantidad de letras que tienen en total

p1 = input("Ingresar palabra 1: ")
p2 = input("Ingresar palabra 2: ")
p3 = input("Ingresar palabra 3: ")
p4 = input("Ingresar palabra 4: ")
p5 = input("Ingresar palabra 5: ")

Palabras = {
    p1:len(p1),
    p2:len(p2),
    p3:len(p3),
    p4:len(p4),
    p5:len(p5)
    }
TotalLetras = Palabras[p1]+Palabras[p2]+Palabras[p3]+Palabras[p4]+Palabras[p5]
print("La cantidad de letras en total es: "+ str(TotalLetras))

