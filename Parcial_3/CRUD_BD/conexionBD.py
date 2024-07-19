import mysql.connector

try:
    conexion=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='bd_python'
    )
except:
    print(f"Ocurrio un Error con el Seridor Por Favor Verifica...")