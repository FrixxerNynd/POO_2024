import mysql.connector

try:
#conectar con la BD en MySQL
    conexion=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='bd_python'
)
except Exception as e:
    # print(f"Error: {e}")
    print(f"Tipo de excepcion: {type(e).__name__}")
    print(f"Ocurrio un error con el seridor ...Por Favor Verifica...")
#verificar si la conexion fue exitosa
else:
    if conexion.is_connected():
        print("se creo la conexion con la BD exitosamente...")
    else:
        print("no fue posible conectar con la BD ...verifique...")