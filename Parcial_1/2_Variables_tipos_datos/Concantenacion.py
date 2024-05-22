#formas de Concatenacion en python

nombre = "Fernando Chavez"
especialidad = "Area de SW"
Carrera = "Desarollo en Gestion y Desarollo de SW"

#1er forma
print("Mi Nombre es "+nombre+" estoy en la especialidad de "+especialidad+" en la carrera de "+Carrera)
print ("\n")


#2da forma
print("Mi Nombre es ",nombre," estoy en la especialidad de ",especialidad," en la carrera de ",Carrera) 
print ("\n")


#3er forma MAS COMUN EN PYTHON
print("Mi Nombre es ",{nombre}," estoy en la especialidad de ",{especialidad}," en la carrera de ",{Carrera}) 
print ("\n")


#4ta forma
print("Mi Nombre es ",{}," estoy en la especialidad de ",{}," en la carrera de ",{},format(nombre, especialidad, Carrera)) 
print ("\n")

#5ta forma
print("Mi nombre es "+nombre+" estoy en la especialidad de "+especialidad+"en la carrera de "+Carrera)
print ("\n")