from coches import *
#Crear un objetos o instanciar la clase

print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
coche1.getInfo()


print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",180,150,5)
coche2.getInfo()


print("Objeto 3")
coche3=Coches("Azul","Audi","2025",240,300,6)
coche3.getInfo()
coche3.setColor("Azul Metalico")
coche3.getInfo()