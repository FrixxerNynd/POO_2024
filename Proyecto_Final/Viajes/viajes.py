from conexionBD import *

class Viaje:
    def __init__(self, id_viaje, destino, salida, costo, hora_partida, estado_viaje, num_turistas):
        self.id_viaje = id_viaje
        self.estado_viaje = estado_viaje        
        self.destino = destino
        self.salida = salida
        self.costo = costo
        self.hora_partida = hora_partida
        self.num_turistas = num_turistas


    def getIdViaje(self):
        return self.id_viaje
    def setIdViaje(self, id_viaje):
        self.id_viaje = id_viaje

    def getEstadoViaje(self):
        return self.estado_viaje
    def setEstadoViaje(self,estado_viaje):
        self.estado_viaje = estado_viaje

    def getDestino(self):
        return self.destino
    def setDestino(self, destino):
        self.destino = destino

    def getSalida(self):
        return self.salida
    def setSalida(self, salida):
        self.salida = salida

    def getCosto(self):
        return self.costo
    def setCosto(self, costo):
        self.costo = costo

    def getHoraPartida(self):
        return self.hora_partida
    def setHoraPartida(self,hora_partida):
        self.hora_partida = hora_partida
    
    def getNumTuristas(self):
        return self.num_turistas
    def setNumTuristas(self, num_turistas):
        self.num_turistas = num_turistas
    
    def crearviaje(self):
        try:
            cursor.execute(
                "INSERT INTO viaje VALUES(%s,%s,%s,%s,%s,%s,%s)",
                (self.id_viaje, self.destino, self.salida, self.costo, self.hora_partida, self.estado_viaje, self.num_turistas)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminarviaje(id_viaje):
        try:
            cursor.execute(
                "DELETE FROM viaje WHERE id_viaje= %s",
                (id_viaje,)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def mostrarviajes():
        try:
            cursor.execute(
                "SELECT * FROM viaje"
            )
            muestra = cursor.fetchall()
            return muestra
        except:
            return False
