from conexionBD import *

try:
    micursor = conexion.cursor()

    sql = "UPDATE FROM clientes SET direccion = 'Col.Nueva Vizcaya' WHERE id =1"
    micursor.execute(sql)

    conexion.commit()

except:
    print(f"Ocurrio un problema... porfavor verifica")

else:
    print("Registro Actualizado exitosamente")