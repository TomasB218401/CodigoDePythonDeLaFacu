#funcion que recibe numero y retorna true o false
#si es capicula

def escapi(num):
    newnum = num[::-1]
    resultado = newnum == num
    return resultado

num = "111"

ok = escapi(num)
print(ok)