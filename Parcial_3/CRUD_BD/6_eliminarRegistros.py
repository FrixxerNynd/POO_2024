from conexionBD import *

try:
    micursor = conexion.cursor()

    sql = "DELETE FROM clientes WHERE id = 3"
    micursor.execute(sql)

    conexion.commit()

except:
    print(f"Ocurrio un problema... porfavor verifica")

else:
    print("Registro eliminado exitosamente")