#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

# Solicitar al usuario dos números
numero_inicio = int(input("Ingrese el primer número: "))
numero_fin = int(input("Ingrese el segundo número (Mayor al primer numero): "))

print(f"Números impares entre {numero_inicio} y {numero_fin}:")


for numero in range(numero_inicio, numero_fin):
    if numero % 2 != 0:
        print(numero)