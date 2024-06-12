#3.- 

#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir el contenido de la lista en mayusculas


lista = []


if len(lista) <= 0:
    print("La lista está vacía. Vamos a llenarla con palabras o frases.")

    while True:
        entrada = input("Ingrese una palabra o frase (o 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        lista.append(entrada)

    print("Contenido de la lista:")
    for elemento in lista:
        print(elemento.upper())
else:
    print("La lista ya contiene elementos.")
    print("Contenido de la lista:")
    for elemento in lista:
        print(elemento.upper())