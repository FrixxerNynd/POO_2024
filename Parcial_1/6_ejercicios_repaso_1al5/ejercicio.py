# Crear un programa que calcule y obtenga el total a pagar por un producto determinado. Se debera de solicitar el nombre o descripcion del producto, codigo, cantidad del producto, precio unitario. 
# El total a pagar incluye el iva(16%) y el descuento.
# Si se compran de 1 a 5 productos se otorga el 10% de descuento, si son de 6 a 10 el 15% de descuento, si se compran mas de 10 el 20% de descuento.

Nproducto = input("El nombre del producto: ")
Descproducto = input("Ingresa la descripcion del producto (marca, cantidad, etc): ")
Codproducto = int(input("Ingresa el codigo del producto: "))
Cantproducto = int(input("Ingresa la cantidad unitaria del producto: "))
Precproducto = int(input("Ingresa el precio del producto: "))


iva = 0.16
if Cantproducto >=1 & Cantproducto < 5:
    descuento = Precproducto * 0.10
    Precio = (Precproducto * iva) - descuento

    print(Precio)