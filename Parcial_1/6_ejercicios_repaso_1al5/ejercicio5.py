#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

min = int(input("Ingresa un numero: \n "))
max = int(input("Ingresa un numero mayor al anterior: \n "))

for i in range(min, max+1):
    print(f"Los numeros son: {i}")