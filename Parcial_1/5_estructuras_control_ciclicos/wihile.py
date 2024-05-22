"""
El ciclo while es una estructura de control que itera o repite la ejecucion de una serie de instrucciones veces como la condicion se cumpla 'true'

Sintaxis:
while condicion:
    bloque de instrucciones
"""

#Ejemplo 1 crear un programa que imprima 5 veces el caracter @

contador = 1
while contador <= 5:
    print("@")
    contador += 1

#Ejemplo 2 crear un programa que imprima los numeros del 1 al 5, los sume y al final imprima la suma
suma = 0
contador = 1

while contador <= 5:
    print(contador)
    suma += contador
    contador += 1
    print()

    #Ejemplo 3 crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente.
    numero = input("Ingrese el numero: ")
    contador = 0
    multi = 0
    while contador <= 10:
        multi = numero * contador
        print(f"El resultado de la multiplicacion {numero} por {contador} es: {multi}")
        multi += 1
        contador += 1