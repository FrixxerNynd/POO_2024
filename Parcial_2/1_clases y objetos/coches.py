"""
Programación Orientada a a Objetos POO o OOP

    Clases: es como un molde a traves del cual se puede instanciar un objeto. Dentro de las clases se 
    definen atributos (propiedades/características) y los métodos (funciones o acciones)

    Objetos o instancias: son parte de una clase, los objetos o instancias pertenecen a una clase
    es decir interactuan con la clase o clases y hacer uso de los atributos y métodos es necesario
    crear un objeto u objetos
"""

"""
Pregunta: ¿Porque y cuando se recomienda usar un metodo getter y setter? 
Los Getters y Setters nos permiten leer y escribir (respectivamente) los valores 
de nuestras variables privadas desde fuera de la clase donde fueron creadas. 
Con los Getters obtenemos los datos de las variables y con los Setters asignamos o cambiamos su valor
"""

#Ejemplo 1 - Crear una clase (un molde para crear mas objetos) llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:
    
    #Atributos o propiedades
    #Caracteristicas del coche
    #Valores iniciales es posible declarar al principio de una clase
    
    color = "Rojo"
    marca = "Ferrari"
    modelo = "2010"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    #Metodos o acciones o funciones o acciones que hace el objeto
    
    def acelerar(self):
        self.velocidad += 1
        
        
    def frenar(self):
        self.velocidad -= 1
    
#Fin definir clase

#Crear un objetos o instanciar la clase
coche1 = Coches()

#Mostrar los valores inicales del objeto o instancia de la clase
print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas}\n Modelo: {coche1.modelo} con una velocidad de {coche1.velocidad} KM/h y una potencia de {coche1.caballaje} HP")

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
   coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

coche2 = Coches(), coche2.marca = "Porche"
coche2.color = "Amarillo"
coche2.modelo= "2024"
coche2.velocidad = 600
coche2.caballaje = 550
coche2.plazas = 4

print(f"Marca: {coche2.marca} {coche2.color}, numeros de plazas: {coche2.plazas}\n Modelo: {coche2.modelo} con una velocidad de {coche2.velocidad} KM/h y una potencia de {coche2.caballaje} HP")
