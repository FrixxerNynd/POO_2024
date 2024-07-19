from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="create table clintes2(id int primary key auto_increment,nombre varchar(60),direccion varchar(120),tel varchar(10))"

    micursor.execute(sql)
except:
    print("Occurio un Error Por Favor Verifica...")
else:
    print("Se creo la tabla Exitosamente")