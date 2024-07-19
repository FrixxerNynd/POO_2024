from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="select * from clintes"
    micursor.execute(sql)

    #Crear un objeto para enviar el resultado de la ejecion del esecute para posteriormente mostrar con ciclo
    resultado=micursor.fetchall()
except:
    print("Occurio un Error Por Favor Verifica...")
else:
    for x in resultado:
        print(x)