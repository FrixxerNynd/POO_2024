"""List
Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite miembros duplicados."""
import os
os.system("clear")
#Ejemplo1 - Crear una lista con datos numericos e imprimir el contenido:

lista = [23, 44]

print(lista)

#Recorrer la lista con el for

for i in lista:
    print(i)

#Recorrer la lista con el while
i = 0
while i <= len(lista) - 1 :
    print(lista[i])
    i +=1

#Ejemplo 2 - Crear una lista de 4 palabras, solicitar una palabra y buscar la coincidencia en la lista e indicar si la encontro o no y en que posicion

palabras = ["hola", "2024","Bye", "UTD"]

palabra_buscar = input("Ingresa la palabra a buscar:  ")

Find =True
for i in palabras:
    if palabra_buscar ==i:

        print (f"Se encontro la palabra solicitada en la posicion {palabras.index(i)}")
        print(f"La palabra: {palabra_buscar} fue encontrada dentro de la lista")
        Find = False



if Find:
    print("No encontre la palabra")


print(palabras)

palabra_buscar = input("Ingresa la palabra a buscar:  ")

Find =True
i = 0
while i <= len(palabras)-1:
    if palabra_buscar == palabras[i]:
        print (f"Se encontro la palabra solicitada en la posicion {i}")
        print(f"La palabra: {palabra_buscar} fue encontrada dentro de la lista")
        Find = False
        i += 1
        break

if Find:
    print("No encontre la palabra")



#Ejemplo 3 agregar y eliminar elementos de una lista.
os.system("clear")
numeros = [23, 34]

print(numeros)

#Agregar un elemento
numeros.append(100)
print(numeros)

numeros.insert(3,200)
print(numeros)

#Eliminar un elemento

numeros.remove(100) #indicar el elemento a borrar
print(numeros)