"""
Comentario de varias lineas:
Cuando se imprime en panlla una cadena de caracteres
se trabaja por default con "cadenas" es decir python
no puede concatenar otra cosa que no sea un String (str)

"""
texto = "Soy una cadena de caracteres"
numero = 23

#concatenar str con str

print("Soy otra cadena y "+ texto)

#Concatenar str con int


print("El numero: "+ str(numero))


#Concatenar int con str

n1 = int('23')
n2 = 33

suma = n1 + n2

print("La suma es: "+ str(suma))
print(f"La suma es: {suma}")


#Concatenar float e int con str

n1 = 23
n2 = 33.0

suma = float(n1) + n2

print("La suma es: "+ str(suma))
print(f"La suma es: {suma}")