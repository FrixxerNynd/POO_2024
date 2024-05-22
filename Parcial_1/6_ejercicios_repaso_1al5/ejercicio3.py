# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros  numeros naturales. Resolverlo con while y for
for i in range(1,61):
    result = i * i
    print (f"El resultado de {i} por {i} es: {result}")


Contador = 1
b = 1
while Contador < 60:
    resultado = b * b
    
    b += 1
    Contador += 1

    print(f"El resultado es {resultado}")