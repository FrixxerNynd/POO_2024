"""
Es un ciclo iterativo y se ejecuta x veces de acuerdo a los valores numericos, enteros establecidos.

for variable in elemento iterable )lista, rango, etc):
    bloque de instrucciones

    """
#Ehemplo 1 crear un programa que imprima 5 veces el caracter @

contador = 1

for contador in range(1,6):
    print("@")


#Ejemplo 2 crear un programa que imprima los numeros del 1 al 5, los sume y al final imprima la suma

suma = 0
for numero in range(1,6):
    print(numero)
    suma += numero

print(f"La suma es: {suma}")


#Ejemplo 3 crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente.

numero = input("Ingrese el numero: ")


multi = 0
for contador in range(1,11):
    multi = numero * contador

print(f"El resultado de la multiplicacion {numero} por {contador} es: {multi}")
multi += 1

