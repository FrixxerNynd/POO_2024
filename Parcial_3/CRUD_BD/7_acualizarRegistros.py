from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="update clintes set direccion='Col. Nueva Vizcaya' where id=1;"
    micursor.execute(sql)

    conexion.commit()
except:
    print("Occurio un Error Por Favor Verifica...")
else:
    print("Registro Actualizado Exitosamente")