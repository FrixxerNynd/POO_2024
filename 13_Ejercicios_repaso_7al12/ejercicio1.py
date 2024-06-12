#1.- 
# Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
# a.- Recorrer la lista y mostrarla
# b.- hacer una funcion que recorra la lista de numeros y devuelva un string
# c.- ordenarla y mostrarla
# d.- mostrar su longitud
# e.- buscar algun elemento que el usuario pida por teclad


def RecorreryDevolver():
    
    for i in lista_numeros:
        a = str(i)
        print(a)
        print(type(a))   

lista_numeros = [8,24,67,8,53,4,6,478]


print(lista_numeros)
for i in lista_numeros:
    print(i)

RecorreryDevolver()

print("Lista no ordenada: \n",lista_numeros)
lista_numeros.sort
print("Lista ordenada: \n",lista_numeros)

print("La longitud de la lista es :", len(lista_numeros))

numero_buscar = int(input("Ingresa el numero a buscar:  "))

Find =True
i = 0
while i <= len(lista_numeros)-1:
    if numero_buscar == lista_numeros[i]:
        print (f"Se encontro el numero solicitado en la posicion {i}")
        print(f"El numero: {numero_buscar}fue encontrado dentro de la lista")
        Find = False
        
        break
    i += 1
if Find:
    print("No encontre la palabra")