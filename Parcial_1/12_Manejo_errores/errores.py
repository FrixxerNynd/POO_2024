#Los errores de excepciones en un lenguaje de programacion no es otra cosa que los errores en tiempo de ejecucion... Cuando se 
#manejan los errores mediante las excepciones en realidad se dice que se evita que se presenten esos errores en programa
#en tiempo ejecucion

#Ejemplo: Se presenta un error cuando no es generada una variable

try:
    nombre = input('Dame el nombre completo de una persona: ')

    if len(nombre)>0:
        nombre_usuario='El nombre del usuario del sistema es: '+ nombre
    
        print(nombre_usuario)
except:
    print("Ingresa un nombre valido")
    
#Ejemplo 2: Cuando se solicita un numero y se ingresa otra cosa

try:
    numero = int(input("Ingresa un numero entero: "))

    if numero>0:
        print("Soy un numero entero positivo")
    else:
        print("Soy un numero entero negativo")
except ValueError:
    print("No es posible convertir una letra a un numero, verifica por favor...")
    
#Ejemolo 3: Cuando se generan multiples excepciones

try:
    numero=int(input('Ingresa un numero: '))
    
    print('El cuadrado del numero es:'+ str(numero * numero))
    
except TypeError:
    print("Es necesario convertir el numero a entero")
    
except ValueError:
    print("No es posible convertir una letra a un numero, verifica por favor...")
    
else: 
    print('Todo se ejecuto correctamente')
    
finally:
    print('Ya termino')
