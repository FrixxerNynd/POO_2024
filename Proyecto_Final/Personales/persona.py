class Persona:
    def __init__(self, nombre, apellidos, edad, genero):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.genero = genero

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellidos(self):
        return self.apellidos
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad

    def getGenero(self):
        return self.genero
    def setGenero(self, genero):
        self.genero = genero

