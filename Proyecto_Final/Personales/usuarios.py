from conexionBD import *



class Usuario:
    def __init__(self, nombre,email,password):
        self.nombreUsuario = nombre
        self.email = email
        self.contraseña =password
    
    #Funcion para encriptar la contraseña

   
    def registrar(self):
        try:
            cursor.execute(
                "insert into usuarios values (null,%s,%s,%s)",
                (self.nombreUsuario,self.email,self.contraseña)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email, contraseña):
            try:
                cursor.execute(
                      "SELECT * FROM usuarios WHERE correo=%s and contrasena=%s",
                      (email, contraseña)
                 )
                usuario = cursor.fetchone()
                if usuario:
                    return usuario
                else:
                    return None    
            except:    
                return None  
        

