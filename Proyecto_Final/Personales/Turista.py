from Personales.persona import *
from conexionBD import *


class Turista(Persona):
    def __init__(self, nombre, apellidos, edad, genero, estancia, id_turista):
        super().__init__(nombre, apellidos, edad, genero)
        self.estancia = estancia
        self.id_turista = id_turista

    def getEstancia(self):
        return self.estancia
    def setEstancia(self, estancia):
        self.estancia = estancia

    def getID(self):
        return self.id_turista
    def setID(self, id_turista):
        self.id_turista = id_turista


    def validarIden(self):
        print(f"La información registrada es la siguiente: \n"
          f"Nombre: {self.getNombre()} \n"
          f"Apellidos: {self.getapellidos()} \n"
          f"Edad: {self.getedad()} \n"
          f"Género: {self.getgenero()} \n"
          f"Estancia de Viaje: {self.getEstancia()}\n"
          f"ID Registrado: {self.getID()}")
        
    def crearTurista(self):
        try:
            cursor.execute(
                "INSERT INTO `turista` VALUES(%s,%s,%s,%s,%s,%s)",
                (self.nombre, self.apellidos, self.edad, self.genero, self.estancia,self.id_turista)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminarTurista(id_turista):
        try:
            cursor.execute(
                "DELETE FROM turista WHERE turista.id_turista=%s",
                (id_turista,)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod    
    def actualizarTurista(nombre, apellidos,edad, genero, id_turista):
        try:
            cursor.execute(
                "UPDATE turista SET nombre=%s, apellidos=%s, edad=%s, genero=%s WHERE id_turista=%s",
                (nombre, apellidos, edad, genero, id_turista)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod    
    def mostrarTuristas():
        try:
            cursor.execute(
                "SELECT * FROM turista WHERE 1"
                
            )
            muestra = cursor.fetchall()
            return muestra
        except:
            return False
        