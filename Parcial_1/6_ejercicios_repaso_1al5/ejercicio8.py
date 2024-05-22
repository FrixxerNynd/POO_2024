#acer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?


numero = float(input("Ingrese el número: "))
porcentaje = float(input("Ingrese el porcentaje a calcular (en %): "))

resultado = (porcentaje / 100) * numero


print(f"{porcentaje}% de {numero} es: {resultado}")