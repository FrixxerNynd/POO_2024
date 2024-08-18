from conexionBD import *

class ReservaViaje:
    def __init__(self, id_viaje, id_turista):
        self.id_viaje = id_viaje
        self.id_turista = id_turista
    
    def crearReserva(self):
        try:
            cursor.execute(
                "INSERT INTO reservaviaje VALUES (NULL, %s, %s)",
                (self.id_viaje, self.id_turista)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminarReserva(folio):
        try: 
            cursor.execute(
                "DELETE FROM reservaviaje WHERE folio =%s",
                (folio,)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def mostrarReservas():
        try:
            cursor.execute(
                "SELECT * FROM reservaviaje"
            )
            muestra = cursor.fetchall()
            return muestra
        except:
            return False