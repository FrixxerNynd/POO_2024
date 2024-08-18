from conexionBD import *


class ReservaPaseo:
    def __init__(self, id_ruta, id_guia, id_turista, id_viaje):
        self.id_ruta = id_ruta
        self.id_guia = id_guia
        self.id_turista = id_turista
        self.if_viaje = id_viaje

    def crearReserva(self):
        try:
            cursor.execute(
                "INSERT INTO reservapaseo VALUES (NULL, %s,%s,%s,%s)",
                (self.id_ruta, self.id_guia, self.id_turista, self.if_viaje)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def mostrarReservas():
        try:
            cursor.execute(
                "SELECT* FROM reservapaseo"
            )
            muestra = cursor.fetchall()
            return muestra
        except:
            return False
    
    @staticmethod
    def eliminarReservas(folio):
        try:
            cursor.execute(
                "DELETE FROM reservapaseo WHERE folio=%s",
                (folio,)
            )
            conexion.commit()
            return True
        except:
            return False
        