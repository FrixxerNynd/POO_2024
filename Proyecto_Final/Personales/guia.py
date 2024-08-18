from conexionBD import *
from Personales.persona import *

class Guia(Persona):
    def __init__(self, nombre, apellidos, edad, genero, experiencia, idioma, tarifa, id_guia):
        super().__init__(nombre, apellidos, edad, genero)
        self.experiencia = experiencia
        self.idioma = idioma
        self.tarifa = tarifa
        self.id_guia = id_guia  

   
    def getExperiencia(self):
        return self.experiencia
    def setExperiencia(self,experencia):
        self.experiencia = experencia

    def getIdioma(self):
        return self.idioma
    def setIdioma(self, idioma):
        self.idioma = idioma

    def getTarifa(self):
        return self.tarifa
    def setTarifa(self, tarifa):
        self.tarifa = tarifa

    def validarIden(self):
        print(f"La información registrada es la siguiente: \n"
          f"Nombre: {self.getNombre()} \n"
          f"Apellidos: {self.getapellidos()} \n"
          f"Edad: {self.getedad()} \n"
          f"Género: {self.getgenero()} \n"
          f"Experiencia: {self.getExperiencia()} \n"
          f"Idioma: {self.getIdioma()} \n"
          f"Tarifa: {self.getTarifa()}")

    def crearGuia(self):
        try:
            cursor.execute(
                "INSERT INTO guia VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.nombre, self.apellidos, self.edad, self.genero,self.experiencia, self.idioma,self.tarifa,self.id_guia)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod    
    def eliminarGuia(id_guia):
        try:
            cursor.execute(
                "DELETE FROM guia WHERE id_guia= %s",
                (id_guia,)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod    
    def actualizarGuia(nombre, apellidos, edad, genero, id_guia):
        try:
            cursor.execute(
                "UPDATE guia SET nombre=%s, apellidos=%s, edad=%s, genero=%s WHERE id_guia=%s",
                (nombre, apellidos, edad, genero, id_guia)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def mostrarGuias():
        try:
            cursor.execute(
                "SELECT * FROM guia"
                
            )
            muestra = cursor.fetchall()
            return muestra
        except:
            return False
        