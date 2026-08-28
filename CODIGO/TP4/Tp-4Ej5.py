#Definir una función que calcule el perímetro de un hexágono regular,
#la función devuelve el
#perímetro. Que parámetros debe contener la función y porque?

def perim_hexan_regu(lado):
    perimetro = (lado * 6)
    return perimetro

lado_hex = float(input("Ingrese el valor de uno de los lados del hexagono regular, para saber su perimetro: "))

perimetro = perim_hexan_regu(lado_hex)

print("El perimetro del hexagono regular es igual a :",str(perimetro))