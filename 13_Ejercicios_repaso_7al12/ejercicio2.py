#2.- 
#Escribir un programa  que añada valores a una lista mientras que su longitud sea menor a 120, y luego mostrar la lista: Usar un while y for
import random
lista =[]

i = 0
while len(lista) < 120:
    for i in range(10):
        lista.append(random.randrange(1,1000,1))
        i += 1

#Muestra de los valores:

print(lista)
