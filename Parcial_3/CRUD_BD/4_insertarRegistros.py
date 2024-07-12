from conexionBD import *

try:
    micursor = conexion.cursor()

    nombre = input("¿Cual es el nombre? ")
    direccion = input("Cual es tu direccion? ")
    tel = input("¿Cual es tu telefono? ")

    #sql = "INSERT INTO clientes (id,nombre,direccion,tel) VALUES (null, 'Daniel Contreras', 'Col. Centro', '1681234567')"
    
    sql = "INSERT INTO clientes (id,nombre,direccion,tel) VALUES (null, %s, %s, %s)"
    valores = (nombre, direccion, tel)
    micursor.execute(sql, valores)

    #Sirve para finalizar la ejecucion del SQL
    conexion.commit()
except:
    print(f"Ocurrio un problema... porfavor verifica")

else:
    print ("Registro insertado exitosamente")



#Para resetear un valor incrementable se utiliza el "ALTER TABLE nombre_tabla AUTO_INCREMENT = 1"