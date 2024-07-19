import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
    )

except:
    print(f"Ocurrio un Error con el Seridor Por Favor Verifica...")
else:
    #Crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
    micursor=conexion.cursor()

    sql="create database bd_python"
    #Ejecutar la consulta SQL
    micursor.execute(sql)

    if micursor:
        print("Se creo la BD exitosamente")

    #mostrar las BD que existen e  el SGBD MySQL
    micursor.execute("show database")
    for x in micursor:
        print(x)