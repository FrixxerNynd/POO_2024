from usuarios import usuario
from notas import nota
import getpass
from funciones import *

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cual es tu nombre?: ")
            apellidos = input("\t ¿Cuales son tus apellidos?: ")
            email = input("\t Ingresa tu email: ")
            password = getpass.getpass("\t Ingresa tu contraseña: ")

            obj_usuario = usuario.Usuario(nombre,apellidos,email,password)
            resultado = obj_usuario.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos} se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")    
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email = input("\t Ingresa tu E-mail: ")
            password = getpass.getpass("\t Ingresa tu Contraseña: ")

            # obj_usuario=usuario.Usuario("","",email,password)
            registro = usuario.Usuario.iniciar_sesion(email,password)
            if registro:
               menu_notas(registro[0],registro[1],registro[2])
            else:
               print(f"\n\t ** Nombre de usuario y/o contraseña incorrectos, intentalo de nuevo ** ...")
               esperarTecla()          
        elif opcion == '3':
            print("\n\t.. ¡Gracias Bye! ...")
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Notas ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")

            obj_nota = nota.Nota(usuario_id, titulo, descripcion)
            resultado = obj_nota.crear()
            if resultado:
                print(f"\n \t \t..:: La nota {titulo} se creó correctamente ::..")
            else:
                print(f"\n \t \t...** No fue posible crear la nota {titulo} por favor verifique **...")
            esperarTecla()

        elif opcion == '2':
            borrarPantalla()

            registro = nota.Nota.mostrar()
            if registro:
                print(f"\n \t \t  {nombre} {apellidos} Aquí estan tus notas:  ")
                num_nota = 1
                for fila in registro:
                    print(f"\t #Nota: {num_nota} \n ID: {fila[0]}.- Titulo: {fila[2]}.- Fecha: {fila[4]}.- \n Descripcion: {fila[3]}\n\n")
                    num_nota+=1
            else:
                print(f"...** El usuario {nombre} {apellidos} no tiene notas **...")
            esperarTecla()

        elif opcion == '3':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")

            resultado = nota.Nota.actualizar(id, titulo, descripcion)
            if resultado:
                print(f"\n \t .:: La nota se ha actualizado correctamente ::.")
            else:
                print(f"\n \t \t...** No fue posible actualizar la nota, por favor verifique **...")
            esperarTecla()
        elif opcion == '4':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")

            resultado = nota.Nota.eliminar(id, titulo, descripcion)
            if resultado:
                print(f"\n \t .:: La nota se ha eliminado correctamente ::.")
            else:
                print(f"\n \t \t...** No fue posible eliminar la nota, por favor verifique **...")
            esperarTecla()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
  menu_principal()

