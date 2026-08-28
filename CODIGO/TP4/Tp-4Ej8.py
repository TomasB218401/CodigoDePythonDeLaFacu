#funcion que recibe como parametro una cifra y
#devuelve la cifra a dolares
#en este caso tomare el peso como cifra
#y el dolar vale 1400

def conversion_dolar(cifra,tasacambio):
    dolar = cifra / tasacambio
    return dolar



total = conversion_dolar(50000,1400)

print("La tasa en dolares es: $",str(total)[0:5])