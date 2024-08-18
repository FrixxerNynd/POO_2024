from conexionBD import *
import datetime

class PaseoTuristas:
    def __init__(self, id_ruta, tiempo, id_guia, estado_paseo, destino, costo, hora_partida):
        self.tiempo = tiempo
        self.id_guia = id_guia
        self.id_ruta = id_ruta
        self.estado_paseo = estado_paseo
        self.destino = destino
        self.costo = costo
        self.hora_partida = hora_partida

    def getTiempo(self):
        return self.tiempo

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def getGuia(self):
        return self.guia

    def setGuia(self, guia):
        self.guia = guia

    def getIdRuta(self):
        return self.id_ruta

    def setIdRuta(self, id_ruta):
        self.id_ruta = id_ruta
    
    def getEstadoPaseo(self):
        self.estado_paseo
    def setEstadoPaseo(self, estado_paseo):
        self.estado_paseo = estado_paseo

    def crearpaseo(self):
        try:
            cursor.execute(
                "INSERT INTO paseoturistas VALUES(%s,%s,%s,%s,%s,%s,%s)",
                (self.id_ruta, self.tiempo, self.id_guia, self.estado_paseo, self.destino, self.costo, self.hora_partida)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminarpaseo(id_ruta):
        try:
            cursor.execute(
                "DELETE FROM paseoturistas WHERE id_ruta= %s",
                (id_ruta)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def mostrarpaseos():
        try:
            cursor.execute(
                "SELECT * FROM paseoturistas"
            )
            muestra = cursor.fetchall()
            return muestra
        except:
            return False