from conexionBD import *

try:
    micursor=conexion.cursor()
    nombre=input("Cual es tu nombre: ")
    direes=input("Cual es tu direccion: ")
    tel=input("Cual es tu telefono: ")
    # sql="INSERT INTO `clintes` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, 'Daniel Contreras', 'col Cento', '6181234567');"
    sql="INSERT INTO `clintes` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL,%s,%s,%s);"
    valores=(nombre,direccion,tel)
    micursor.execute(sql,valores)

    #sirve para finalizar la ejecucion del SQL
    conexion.commit()
except:
    print("Occurio un Error Por Favor Verifica...")
else:
    print(f"Registro insertado Exitosamente")