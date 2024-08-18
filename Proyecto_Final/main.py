from Paseos import PaseoTuristico
from Personales import Turista, usuarios
from Personales import guia
from Viajes import viajes
from funciones import *
from Reservaciones import reservarPaseo, reservarViaje

def menu_inicio():
    while True:
        print("""
      .::  Menu Principal ::. 
          1.- Registrar
          2.- Iniciar Sesion
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cual sera tu nombre de usuario (Evita malas palabras o palabras ofensivas)?: ")
            email = input("\t Ingresa tu email: ")
            password = input("\t Ingresa tu contraseña: ")

            obj_usuario = usuarios.Usuario(nombre,email,password)
            resultado = obj_usuario.registrar()
            if resultado:
                print(f"\n\t {nombre} se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")    
            esperarTecla()

        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email = input("\t Ingresa tu E-mail: ")
            password = input("\t Ingresa tu Contraseña: ")

            registro = usuarios.Usuario.iniciar_sesion(email,password)
            if registro:
               menu_principal()
            else:
               print(f"\n\t ** E-mail y/o contraseña incorrectos, intentalo de nuevo ** ...")
               esperarTecla()          
        elif opcion == '3':
            print("\n\t.. ¡Gracias Bye! ...")
            break
            
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()


def menu_reservar():
    while True:
        borrarPantalla()
        print("""
                \t..:::|MENU RESERVAS|::..
              1. Reservar un Viaje
              2. Reservar un Paseo
              3. Eliminar un Viaje
              4. Eliminar un Paseo
              5. Mostrar todos los Viajes Reservados
              6. Mostrar todos los paseos Reservados
              7. Salir
            """)

        opcion = input("Ingresa una Opcion: ")
        if opcion == '1':
            print("\t|----- Reserva de Viaje -----|")
            id_viaje = input("Ingresa el ID del viaje a relacionar en la reserva: ")
            id_turista = input("Ingresa el ID del turista que solicito la reserva: ")
            obj_reserva = reservarViaje.ReservaViaje(id_viaje, id_turista)

            resultado = obj_reserva.crearReserva()
            if resultado:
                print(f"\n \t \t..:: Se ha realizado la reserva correctamente ::..")
            else:
                print(f"\n \t \t...** No fue posible realizar la reserva por favor verifique los datos e intente nuevamente **...")
            esperarTecla()

        elif opcion =='2':
            print("\t|----- Reserva de Paseo -----|")
            id_ruta = input("Ingresa el ID de la Ruta a relacionar en la reserva: ")
            id_guia = input("Ingresa el ID del Guia que acompañara el paseo: ")
            id_turista = input("Ingresa el ID del turista que solicito la reserva: ")
            id_viaje = input("Ingresa el ID del viaje al que pertenece la reserva del paseo: ")

            obj_reserva = reservarPaseo.ReservaPaseo(id_ruta, id_guia, id_turista, id_viaje)
            if resultado:
                print(f"\n \t \t..:: Se ha realizado la reserva correctamente ::..")
            else:
                print(f"\n \t \t...** No fue posible realizar la reserva por favor verifique los datos e intente nuevamente **...")
            esperarTecla()

        elif opcion == '3':
            print("\t|----- Eliminacion de Viaje -----|")
            folio = input('Ingresa el folio de la reserva a eliminar: ')

            resultado = reservarViaje.ReservaViaje.eliminarReserva(folio)
            if resultado:
                    print("..:: Reserva Eliminada exitosamente ::..")
            else:
                    print(f"\n \t \t...** No fue posible eliminar la reserva, por favor intente nuevamente **...")
            esperarTecla()

        elif opcion == '4':
            print("\t|----- Eliminacion de Paseo -----|")
            folio = input('Ingresa el folio de la reserva a eliminar: ')

            resultado = reservarPaseo.ReservaPaseo.eliminarReservas(folio)
            if resultado:
                    print("..:: Reserva Eliminada exitosamente ::..")
            else:
                    print(f"\n \t \t...** No fue posible eliminar la reserva, por favor intente nuevamente **...")
            esperarTecla()

        elif opcion == '5':
            print("\t|----- Muestra de Viajes -----|")
            resultado = reservarViaje.ReservaViaje.mostrarReservas()
            if resultado:
                print("\t \t..:: Aqui se muestran todas las reservas")
                num = 1
                for fila in resultado:
                    print(f"\t Reserva #: {num} \n  Folio: {fila[0]}.- ID del Viaje Reservado: {fila[1]}. - ID del turista acreedor de la reserva: {fila[2]}")
                    num +=1
            else:
                    print(f"...** No hay reservas registradas **...")
            esperarTecla()

        elif opcion == '6':
            print("\t|----- Muestra de Paseos -----|")
            resultado = reservarPaseo.ReservaPaseo.mostrarReservas()
            if resultado:
                print("\t \t..:: Aqui se muestran todas las reservas")
                num = 1
                for fila in resultado:
                    print(f"\t Reserva #: {num} \n  Folio: {fila[0]}.- ID del Paseo Reservado: {fila[1]}. - ID del Guia seleccionado: {fila[2]}. - ID del turista acreedor de la reserva: {fila[3]}. - ID del Viaje perteneciente a la Reserva: {fila[4]}")
                    num +=1
            else:
                    print(f"...** No hay reservas registradas **...")
            esperarTecla()
        elif opcion == '7':
            break

def menu_principal():
    while True:
        borrarPantalla()
        print("\n\t..::-- MENU--::..")
        print("1. Crear turista")
        print("2. Modificar turista")
        print("3. Eliminar turista")
        print("4. Mostrar turistas")
        print("5. Crear guía")
        print("6. Modificar guía")
        print("7. Eliminar guía")
        print("8. Mostrar guías")
        print("9. Crear viaje")
        print("10. Eliminar viaje")
        print("11. Mostrar viajes")
        print("12. Crear Paseo Turistico")
        print("13. Eliminar Paseo Turistico")
        print("14. Mostrar Paseos Turisticos")
        print("15. Realizar Reservaciones")
        print("16. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            print("\t|----- Creacion de Turista -----|")
            nombre = input("Ingrese el nombre del turista: ")
            apellidos = input("Ingrese los apellidos del turista: ")
            edad = int(input("Ingrese la edad del turista: "))
            genero = input("Ingrese el género del turista: ")
            estancia = input("Ingrese la estancia del turista: ")
            id_turista = input("Ingrese el ID del turista: ")
            obj_turista = Turista.Turista(nombre, apellidos, edad, genero, estancia, id_turista)
            
            resultado = obj_turista.crearTurista()
            if resultado:
                print(f"\n \t \t..:: El turista fue registrado correctamente ::..")
            else:
                print(f"\n \t \t...** No fue posible registrar al turista por favor verifique los datos e intente nuevamente **...")
            esperarTecla()

        elif opcion == '2':
            print("\t|----- Modificacion de Turista -----|")
            id_turista = input("Ingrese el ID del turista: ")
            nombre = input("Ingrese el nombre del turista: ")
            apellidos = input("Ingrese los apellidos del turista: ")
            edad = int(input("Ingrese la edad del turista: "))
            genero = input("Ingrese el género del turista: ")

            resultado = Turista.Turista.actualizarTurista(nombre, apellidos, edad, genero, id_turista)
            if resultado:
                print(f"\n \t \t..:: Los datos se modificaron correctamente ::..")
            else:
                print(f"\n \t \t...** No fue posible modificar la informacion,por favor verifique los datos e intente nuevamente **...")
            esperarTecla()
        elif opcion == '3':
            print("\t|----- Eliminacion de Turista-----|")
            id_turista = input("Ingrese el ID del turista a Eliminar: ")

            resultado = Turista.Turista.eliminarTurista(id_turista=id_turista)
            if resultado:
                print("..:: Turista Eliminado exitosamente ::..")
            else:
                print(f"\n \t \t...** No fue posible eliminar el turista, por favor intente nuevamente **...")
            esperarTecla()

        elif opcion == '4':
            registro = Turista.Turista.mostrarTuristas()
            if registro:
                print(f"\n \t \t  Aquí estan los turistas registrados:  ")
                num = 1
                for fila in registro:
                    print(f"\t Turista#: {num} \n Nombre: {fila[0]}.- Apellidos: {fila[1]}.- Edad: {fila[2]}.- Genero: {fila[3]}.- Estancia: {fila[4]}.- ID: {fila[5]} \n")
                num+=1
            else:
                print(f"...** No hay turistas registrados **...")
            esperarTecla()

        elif opcion == '5':
            print("\t|----- Creacion de Guias -----|")
            nombre = input("Ingrese el nombre del guía: ")
            apellidos = input("Ingrese los apellidos del guía: ")
            edad = int(input("Ingrese la edad del guía: "))
            genero = input("Ingrese el género del guía (Masculino/Femenino): ")
            experiencia = input("Ingrese la experiencia del guía: ")
            idioma = input("Ingrese el idioma del guía: ")
            tarifa = float(input("Ingrese la tarifa del guía: "))
            id_guia = input("Ingrese el ID correspondiente al Guia: ")
            obj_guia = guia.Guia(nombre, apellidos, edad, genero, experiencia, idioma, tarifa, id_guia)

            resultado = obj_guia.crearGuia()
            if resultado:
                print(f"\n \t \t..:: El Guia fue registrado correctamente ::..")
            else:
                print(f"\n \t \t...** No fue posible registrar al Guia por favor verifique los datos e intente nuevamente **...")
            esperarTecla()
        elif opcion == '6':
            print("\t|----- Modificacion de Guias -----|")
            id_guia = input("Ingrese el ID correspondiente al Guia: ")
            nombre = input("Ingrese el nombre del turista: ")
            apellidos = input("Ingrese los apellidos del turista: ")
            edad = int(input("Ingrese la edad del turista: "))
            genero = input("Ingrese el género del turista: ")

            resultado = guia.Guia.actualizarGuia(nombre, apellidos, edad, genero, id_guia)
            if resultado:
                print(f"\n \t \t..:: Los datos se modificaron correctamente ::..")
            else:
                print(f"\n \t \t...** No fue posible modificar la informacion, por favor verifique los datos e intente nuevamente **...")
            esperarTecla()
        elif opcion == '7':
            print("\t|----- Eliminacion de Turista-----|")
            id_guia = input("Ingrese el ID del guia a Eliminar: ")

            resultado = guia.Guia.eliminarGuia(id_guia)
            if resultado:
                print("..:: Guia Eliminado exitosamente ::..")
            else:
                print(f"\n \t \t...** No fue posible eliminar el Guia, por favor intente nuevamente **...")
            esperarTecla()

        elif opcion == '8':
            registro = guia.Guia.mostrarGuias()
            if registro:
                print(f"\n \t \t  Aquí estan los Guias registrados:  ")
                num = 1
                for fila in registro:
                    print(f"\t Guia#: {num} \n Nombre: {fila[0]}.- Apellidos: {fila[1]}.- Edad: {fila[2]}.- Genero: {fila[3]}.- Experiencia: {fila[4]}.- Idioma: {fila[5]}.- Tarifa: {fila[6]}.- ID: {fila[7]}\n")
                num+=1
            else:
                print(f"...** No hay Guias registrados **...")
            esperarTecla()
        elif opcion == '9':
            print("\t|----- Creacion de Viaje-----|")
            id_viaje = input("Ingrese el ID del viaje: ")
            destino = input("Ingrese el destino del viaje: ")
            salida = input("Ingrese la fecha desalida del viaje (En formato DD-MM-AA): ")
            costo = float(input("Ingrese el costo del viaje: "))
            hora_partida = input("Ingrese la hora de partida del viaje (Formato 24hrs): ")
            estado_viaje = input("Ingrese el estado del viaje: ")
            num_turistas = input("Ingrese el numero maximo de turistas que van a viajar: ")
            obj_viaje = viajes.Viaje(id_viaje, destino, salida, costo, hora_partida, estado_viaje, num_turistas)
          
            resultado = obj_viaje.crearviaje()
            if resultado:
                print(f"\n \t \t..:: El Viaje fue registrado correctamente ::..")
            else:
                print(f"\n \t \t...** No fue posible registrar el viaje por favor verifique los datos e intente nuevamente **...")
            esperarTecla()
        elif opcion == '10':
            print("\t|----- Eliminacion de Viaje-----|")
            id_viaje = input("Ingrese el ID del viaje a Eliminar: ")

            resultado = viajes.Viaje.eliminarviaje(id_viaje)
            if resultado:
                print("..:: Viaje Eliminado exitosamente ::..")
            else:
                print(f"\n \t \t...** No fue posible eliminar el viaje, por favor intente nuevamente **...")
            esperarTecla()

        elif opcion == '11':
            resultado = viajes.Viaje.mostrarviajes()
            if registro:
                print(f"\n \t \t  Aquí estan los Viajes registrados:  ")
                num = 1
                for fila in registro:
                    print(f"\t Viaje#: {num} \n ID: {fila[0]}.- Destino: {fila[1]}.- Salida: {fila[2]}.- Costo: {fila[3]}.- Hora de Partida: {fila[4]}.- Estado del Viaje: {fila[5]}.- Numero de Turistas: {fila[6]}\n")
                num+=1
            else:
                print(f"...** No hay Viajes registrados **...")
            esperarTecla()

        elif opcion == '12':
            id_ruta = input("Ingrese el ID de la ruta del paseo: ")
            tiempo = input("Ingrese el tiempo de duracion del paseo: ")
            Guia = input("Ingrese el guía del paseo: ")
            estado_paseo = input("Ingrese el estado del paseo : ")
            destino = input("Ingrese el Destino del paseo: ")
            costo = input("Ingrese el costo del Paseo Turistico: ")
            hora_partida = ("Ingrese la hora de partida del Paseo(Formato 24 hrs):")
            obj_paseo = PaseoTuristico.PaseoTuristas(id_ruta, tiempo, Guia, estado_paseo, destino, costo, hora_partida )

            resultado = obj_paseo.crearpaseo()
            if resultado:
                print(f"\n \t \t..:: El Paseo turistico fue registrado correctamente ::..")
            else:
                print(f"\n \t \t...** No fue posible registrar el Paseo por favor verifique los datos e intente nuevamente **...")
            esperarTecla()
            
        elif opcion == '13':
            id_ruta = input("Ingresa el Id de la ruta de paseo a eliminar: ")
            resultado = PaseoTuristico.PaseoTuristas.eliminarpaseo(id_ruta)
            if resultado:
                print("..:: Paseo Turistico Eliminado exitosamente ::..")
            else:
                print(f"\n \t \t...** No fue posible eliminar el Paseo, por favor intente nuevamente **...")
            esperarTecla()

        elif opcion == '14':
            resultado = PaseoTuristico.PaseoTuristas.mostrarpaseos()
            if registro:
                print(f"\n \t \t  Aquí estan los Viajes registrados:  ")
                num = 1
                for fila in registro:
                    print(f"\t Paseo#: {num} \n ID: {fila[0]}.- Tiempo de Duracion: {fila[1]}.- Guia Seleccionado: {fila[2]}.- Estado del Paseo: {fila[3]}.- Destino del paseo: {fila[4]}.- Costo del Paseo: {fila[5]}.- Hora de Partida: {fila[6]}\n")
                num+=1
            else:
                print(f"...** No hay Viajes registrados **...")
            esperarTecla()

        elif opcion == '15':
            menu_reservar()
        elif opcion == '16':
            break

if __name__ == "__main__":
    menu_inicio()