 #4.- 

 #Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico, y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

def imprimir_tipo_de_dato(variable):
    if isinstance(variable, list):
        print(f"La variable es una lista: {variable}")
    elif isinstance(variable, str):
        print(f"La variable es una cadena: {variable}")
    elif isinstance(variable, int):
        print(f"La variable es un entero: {variable}")
    elif isinstance(variable, bool):
        print(f"La variable es un booleano: {variable}")

lista = [1, 2, 3, 4, 5]
cadena = "Hellouda"
numero = 42
logico = True

imprimir_tipo_de_dato(lista)
imprimir_tipo_de_dato(cadena)
imprimir_tipo_de_dato(numero)
imprimir_tipo_de_dato(logico)