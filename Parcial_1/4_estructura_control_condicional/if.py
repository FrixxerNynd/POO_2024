"""
Existe una estructura de condicion llamada "if" la cual evalua una condicion para encontrar el valor "True" o se cumple la condicion se enjecuta la linea o lineas de codigo.

Tiene 4 variantes de If.

1.- If simple
2.- If compuesto 
3.- if anidado
4.- if y elif
"""

#Ejemplo 1 if simple

color = "rojo"
if color =="rojo":
    print("Soy el color rojo")


#Ejemplo 2 if compuesto

color = "rojo"
if color =="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo")


#Ejemplo 3 if anidado

color = "rojo"
if color == "rojo":
    print("Soy el color rojo")
    if color != "rojo":
        print("Soy otro color")
else:
    print("No soy el color rojo")


#Ejemplo 4 if con elif

color = "rojo"
if color =="rojo":
    print("Soy el color rojo")
elif color == "negro":
    print("No soy el color rojo, soy el color negro")
elif color == "morado":
    print("No soy el color rojo, soy el color morado")
else:
    print("No soy rojo, verde o negro")

    