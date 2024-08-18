import mysql.connector

try:
    conexion=mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '',
    database = 'bd_turismo'
    )
        
    cursor=conexion.cursor(buffered=True)
except Exception as e:
    print(f"Tipo de excepcion: {type(e).__name__}")
    print(f"Ocurrio un error con el seridor ...Por Favor Verifica...")
else:
    if conexion.is_connected():
        print("se creo la conexion con la BD exitosamente...")
    else:
        print("no fue posible conectar con la BD ...verifique...")