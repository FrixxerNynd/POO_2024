import mysql.connector

try:
    conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'bd_python'
)
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de excepcion: {type(e).__name__}")
    print("Ocurrio un error con el servidor... por favor verifique")

else:
    if conexion.is_connected():
        print("Se creo la conexion con la BD exitosamente ...")
    else:
        print("No fue posible crear la conexion con la BD exitosamente ...verifique por favor")
    