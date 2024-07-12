import mysql.connector

try:
    conexion = mysql.connector.conect(
    host = 'localhost',
    user = 'root',
    password = '',
)

except:
    print(f"Ocurrio un error con el sistema... verifique por favor")

else:
        #Crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
    micursor = conexion.cursor()

    sql = 'CREATE DATABASE bd_python'
    micursor.execute(sql)

    if micursor:
        print (f"Se creo la base de datos exotosamente0")

    #Mostrar las BD que existen en el SGBD MySQL
    micursor .execute('SHOW DATABASES')

    for x in micursor:
        print(x)
