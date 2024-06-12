import math
def esperaTecla():
    #Muestra un mensaje
    print("Presiona cualquier tecla para continuar")
    input()


def solicitarDatos():
   print("\n")
   # global n1,n2,ope
   n1=int(input("Numero #1: "))
   n2=int(input("Numero #2: "))
   ope=input("Operacion: ").upper()
   return n1,n2 

def getCalculadora(num1,num2,operacion):
    if operacion=="1" or operacion=="+" or operacion=="SUMA":
        resultado=f"{num1}+{num2}={int(num1)+int(num2)}"
    elif operacion=="2" or operacion=="-" or operacion=="RESTA":
        resultado=f"{num1}-{num2}={int(num1)-int(num2)}"  
    elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
        resultado=f"{num1}*{num2}={int(num1)*int(num2)}"        
    elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
        resultado=f"{num1}/{num2}={int(num1)/int(num2)}"      
    elif operacion == "5" or operacion == "POTENCIA":
        resultado = f"{num1} ^ {num2} = {int(pow(num1,num2))}"
    elif operacion == "6" or operacion == "RAIZ":
        print("¿Que numero deseas usar para la raiz? (Solo se puede seleccionar 1): ")
        respuesta = input()
        if respuesta == "1" or respuesta == "numero 1" or respuesta == "num1":
            resultado = f"La raiz cuadrada de {num1} es: {int(math.sqrt(num1))}"
        elif respuesta == "2" or respuesta == "numero 2" or respuesta == "num2":
            resultado = f"La raiz cuadrada de {num2} es: {int(math.sqrt(num2))}"
    return resultado