from conexionBD import *

try:
    micursor = conexion.cursor()

    sql = 'CREATE TABLE clientes( id int primary key auto_increment, nombre varchar(60), direccion varchar(120), tel varchar(10))'

    micursor.execute(sql)

except:
    print(f"Ocurrio un problema... porfavor verifica")

else:
    print("Se creo la tabla exitosamente")