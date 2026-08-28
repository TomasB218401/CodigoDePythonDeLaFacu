#Crear diccionario Inventario para almacenar productos como clave
#y cantidad como valor
Inventario = {
    "Manzana":100,
    "Banana":90,
    "Frutillas":80
}
#Añadir nuevo producto o sumar cantidad
Inventario["Frutillas"] = 120
Inventario["Melon"] = 20
#Borrar un producto
del(Inventario["Manzana"])

#Mostrar todos los productos
print(Inventario)