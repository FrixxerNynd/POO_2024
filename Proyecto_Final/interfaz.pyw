import tkinter as tk
from tkinter import messagebox
from Paseos import PaseoTuristico
from Personales import Turista, usuarios, guia
from Viajes import viajes
from Reservaciones import reservarPaseo, reservarViaje


def borrarPantalla():
    for widget in root.winfo_children():
        widget.destroy()

def menu_inicio():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Principal")

    tk.Label(root, text="Menú Principal", font=("Arial", 30), width=20, height=2).pack(pady=20)

    tk.Button(root, text="Registrar", command=registrar, font=("Arial", 20), width=20, height=2).pack(pady=20)
    tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion, font=("Arial", 20), width=20, height=2).pack(pady=20)
    tk.Button(root, text="Salir", command=root.quit, font=("Arial", 20), width=20, height=2).pack(pady=20)

def registrar():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Registro en el Sistema")

    tk.Label(root, text="Registro en el Sistema", font=("Arial", 30), width=20, height=2).pack(pady=20)

    tk.Label(root, text="Nombre de usuario:", font=("Arial", 20), width=20, height=2).pack(pady=15)
    nombre = tk.Entry(root, font=("Arial", 20), width=30)
    nombre.pack()

    tk.Label(root, text="Email:", font=("Arial", 20)).pack(pady=15)
    email = tk.Entry(root, font=("Arial", 20), width=20)
    email.pack()

    tk.Label(root, text="Contraseña:", font=("Arial", 20)).pack(pady=15)
    password = tk.Entry(root, show="*", font=("Arial", 20))
    password.pack()

    def registrar_usuario():
        obj_usuario = usuarios.Usuario(nombre.get(), email.get(), password.get())
        resultado = obj_usuario.registrar()
        if resultado:
            messagebox.showinfo("Registro", f"{nombre.get()} se registró correctamente.")
        else:
            messagebox.showerror("Error", "No fue posible registrar al usuario. Inténtelo de nuevo.")

    tk.Button(root, text="Registrar", command=registrar_usuario, font=("Arial", 20), width=15, height=2).pack(pady=15)
    tk.Button(root, text="Volver al Menú", command=menu_inicio, font=("Arial", 20), width=15, height=2).pack(pady=15)

def iniciar_sesion():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Inicio de Sesión")

    tk.Label(root, text="Inicio de Sesión", font=("Arial", 30), width=30, height=2).pack(pady=20)

    tk.Label(root, text="Email:", font=("Arial", 20)).pack(pady=15)
    email = tk.Entry(root, font=("Arial", 20), width=30)
    email.pack()

    tk.Label(root, text="Contraseña:", font=("Arial", 20)).pack(pady=15)
    password = tk.Entry(root, show="*", font=("Arial", 20))
    password.pack()

    def login():
        registro = usuarios.Usuario.iniciar_sesion(email.get(), password.get())
        if registro:
            menu_principal()
        else:
            messagebox.showerror("Error", "Email y/o contraseña incorrectos.")

    tk.Button(root, text="Iniciar Sesión", command=login, font=("Arial", 20), width=15, height=2).pack(pady=20)
    tk.Button(root, text="Volver al Menú", command=menu_inicio, font=("Arial", 20), width=15, height=2).pack(pady=15)

def menu_principal():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Principal de Opciones")

    tk.Label(root, text="Menú Principal",font=("Arial", 20), width=15, height=2).pack(pady=15)
    tk.Label(root, text="Seleccione una Opcion a la cual desea ingresar", font=("Arial", 20), width=40, height=2).pack(pady=25)
    
    tk.Button(root, text="Turistas", command=menu_turistas, font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Viajes", command=menu_viajes, font=("Arial", 15), width=15, height=1).pack(pady=10)
    
    tk.Button(root, text="Guías", command=menu_guias, font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Paseos Turisticos", command=menu_paseos, font=("Arial", 15), width=15, height=1).pack(pady=10)
    
    tk.Button(root, text="Reservaciones", command=menu_reservar, font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Salir", command=menu_inicio, font=("Arial", 15), width=15, height=1).pack(pady=10)



def menu_turistas():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Principal de Opciones")

    tk.Label(root, text="..:: Menú Turistas ::..", font=("Arial", 30), width=20, height=2).pack(pady=20)
    tk.Label(root, text="Seleccione una Opcion a la cual desea ingresar",font=("Arial", 20), width=40, height=2).pack(pady=20)
    
    tk.Button(root, text="Crear Turista", command=ventana_crear_turista, font=("Arial", 20), width=15, height=2).pack(pady=15)
    
    tk.Button(root, text="Modificar Turista", command=ventana_modificar_turista, font=("Arial", 20), width=15, height=2).pack(pady=15)
    
    tk.Button(root, text="Eliminar Turista", command=ventana_eliminar_turista, font=("Arial", 20), width=15, height=2).pack(pady=15)
    
    tk.Button(root, text="Mostrar Turistas", command= ventana_mostrar_turista, font=("Arial", 20), width=15, height=2).pack(pady=15)
    tk.Button(root, text="Salir", command=menu_principal, font=("Arial", 20), width=15, height=2).pack(pady=15)


def menu_viajes():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Principal de Opciones")

    tk.Label(root, text="..:: Menú Viajes ::..", font=("Arial", 30), width=15, height=2).pack(pady=15)
    tk.Label(root, text="Seleccione una Opcion a la cual desea ingresar", font=("Arial", 30), width=40, height=2).pack(pady=20)
    
    tk.Button(root, text="Crear Viaje", command=ventana_crear_viaje,font=("Arial", 20), width=15, height=2).pack(pady=15)
    
    tk.Button(root, text="Eliminar Viaje", command=ventana_eliminar_viaje, font=("Arial", 20), width=15, height=2).pack(pady=15)
    
    tk.Button(root, text="Mostrar Viajes", command= ventana_mostrar_viaje, font=("Arial", 20), width=15, height=2).pack(pady=15)
    tk.Button(root, text="Salir", command=menu_principal, font=("Arial", 20), width=15, height=2).pack(pady=15)


def menu_guias():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Principal de Opciones")

    tk.Label(root, text="..:: Menú Guias ::..").pack(pady=10)
    
    tk.Label(root, text="Seleccione una Opcion a la cual desea ingresar", font=("Arial", 30), width=40, height=2).pack(pady=20)
    tk.Button(root, text="Crear Guia", command=ventana_crear_guia, font=("Arial", 20), width=15, height=2).pack(pady=15)
    
    tk.Button(root, text="Modificar Guia", command=ventana_modificar_guia, font=("Arial", 20), width=15, height=2).pack(pady=15)
    tk.Button(root, text="Eliminar Guia", command=ventana_eliminar_guia, font=("Arial", 20), width=15, height=2).pack(pady=15)
    
    tk.Button(root, text="Mostrar Guia", command= ventana_mostrar_guia, font=("Arial", 20), width=15, height=2).pack(pady=15)
    tk.Button(root, text="Salir", command=menu_principal, font=("Arial", 20), width=15, height=2).pack(pady=5)

def menu_paseos():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Principal de Opciones")

    tk.Label(root, text="..:: Menú Paseos ::..", font=("Arial", 20), width=20, height=2).pack(pady=10)
    tk.Label(root, text="Seleccione una Opcion a la cual desea ingresar", font=("Arial", 20), width=40, height=2).pack(pady=20)
    
    tk.Button(root, text="Crear Paseo", command=ventana_crear_paseo, font=("Arial", 20), width=15, height=2).pack(pady=15)
    tk.Button(root, text="Eliminar Paseo", command=ventana_eliminar_paseo, font=("Arial", 20), width=15, height=2).pack(pady=15)
    
    tk.Button(root, text="Mostrar Paseos", command= ventana_mostrar_paseos, font=("Arial", 20), width=15, height=2).pack(pady=15)
    tk.Button(root, text="Salir", command=menu_principal, font=("Arial", 20), width=15, height=2).pack(pady=5)
    
def menu_reservar():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Principal de Opciones")

    tk.Label(root, text="..:: Menú Reservas ::..", font=("Arial", 20), width=15, height=2).pack(pady=10)
    tk.Label(root, text="Seleccione una Opcion a la cual desea ingresar", font=("Arial", 20), width=40, height=2).pack(pady=20)

    tk.Button(root, text="Reservar Viaje", command=ventana_reservar_viaje, font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Reservar Paseo", command=ventana_reservar_paseo, font=("Arial", 15), width=15, height=1).pack(pady=10)

    tk.Button(root, text="Eliminar Reserva de Viaje", command=ventana_eliminar_reserva_viaje, font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Eliminar Reserva de Paseo", command=ventana_eliminar_reserva_paseo, font=("Arial", 15), width=15, height=1).pack(pady=10)

    tk.Button(root, text="Mostrar Reservas de Viajes", command=ventana_mostrar_reserva_viaje, font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Mostrar Reservas de Paseos", command=ventana_mostrar_reserva_paseo, font=("Arial", 15), width=15, height=1).pack(pady=10)

    tk.Button(root, text="Salir", command=menu_principal, font=("Arial", 15), width=15, height=1).pack(pady=5)








#Codigo para tabla turista
def ventana_crear_turista():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Turista")

    def crear_turista():
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        edad = entry_edad.get()
        genero = entry_genero.get()
        estancia = entry_estancia.get()
        id_turista = entry_id.get()

        turista = Turista.Turista(nombre, apellidos, edad, genero, estancia, id_turista)
        resultado = turista.crearTurista()
    
        if resultado:
            messagebox.showinfo("Éxito", "El turista fue registrado correctamente.")
        else:
            messagebox.showerror("Error", "No fue posible registrar al turista. Verifique los datos e intente nuevamente.")
        pass

    tk.Label(root, text="Nombre:",font=("Arial", 15), width=15, height=1).grid(row=0, column=0,columnspan=2, pady=10, padx=5)
    entry_nombre = tk.Entry(root, font=("Arial", 15), width=15)
    entry_nombre.grid(row=0, column=1,columnspan=2, pady=10, padx=5)

    tk.Label(root, text="Apellidos:",font=("Arial", 15), width=15, height=1).grid(row=1, column=0, pady=10, padx=5)
    entry_apellidos = tk.Entry(root, font=("Arial", 15), width=15)
    entry_apellidos.grid(row=1, column=1,columnspan=2, pady=10, padx=5)

    tk.Label(root, text="Edad:", font=("Arial", 15), width=15, height=1).grid(row=2, column=0,columnspan=2, pady=10, padx=5)
    entry_edad = tk.Entry(root, font=("Arial", 15), width=15,)
    entry_edad.grid(row=2, column=1,columnspan=2, pady=10, padx=5)

    tk.Label(root, text="Género:", font=("Arial", 15), width=15, height=1).grid(row=3, column=0,columnspan=2, pady=10, padx=5)
    entry_genero = tk.Entry(root, font=("Arial", 15), width=15,)
    entry_genero.grid(row=3, column=1,columnspan=2, pady=10, padx=5)

    tk.Label(root, text="Estancia:", font=("Arial", 15), width=15, height=1).grid(row=4, column=0,columnspan=2, pady=10, padx=5)
    entry_estancia = tk.Entry(root, font=("Arial", 15), width=15)
    entry_estancia.grid(row=4, column=1,columnspan=2, pady=10, padx=5)

    tk.Label(root, text="ID Turista:", font=("Arial", 15), width=15, height=1).grid(row=5, column=0, columnspan=2, pady=10, padx=5, )
    entry_id = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id.grid(row=5, column=1, columnspan=2, pady=10, padx=5)

    tk.Button(root, text="Crear Turista", command=crear_turista, font=("Arial", 15), width=15, height=1).grid(row=7, column=2, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_turistas, font=("Arial", 15), width=15, height=1).grid(row=7, column=3, pady=10, padx=5)

def ventana_modificar_turista():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Turista")

    def modificar_turista():
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        edad = entry_edad.get()
        genero = entry_genero.get()
        id_turista = entry_id.get()

        resultado = Turista.Turista.actualizarTurista(nombre, apellidos, edad, genero, id_turista)
        if resultado:
            messagebox.showinfo("Exto","..:: Los datos se modificaron correctamente ::..")
        else:
            messagebox.showerror("Exito","...** No fue posible modificar la informacion,por favor verifique los datos e intente nuevamente **...")
            
            

    tk.Label(root, text=" ..:: Modificacion de Turistas ::..", font=("Arial", 15), width=25, height=1).grid(row=0, column=1, pady=10)

    tk.Label(root, text="ID Turista para Modificar:", font=("Arial", 15), width=20, height=1).grid(row=1, column=0, pady=10, padx=5)
    entry_id = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id.grid(row=1, column=1, pady=10, padx=5)
    
    tk.Label(root, text="Nombre:", font=("Arial", 15), width=15, height=1).grid(row=2, column=0, pady=10, padx=5)
    entry_nombre = tk.Entry(root, font=("Arial", 15), width=15)
    entry_nombre.grid(row=2, column=1, pady=5, padx=5)
    
    tk.Label(root, text="Apellidos:", font=("Arial", 15), width=15, height=1).grid(row=3, column=0, pady=10, padx=5)
    entry_apellidos = tk.Entry(root, font=("Arial", 15), width=15)
    entry_apellidos.grid(row=3, column=1, pady=10, padx=5)

    tk.Label(root, text="Edad:", font=("Arial", 15), width=15, height=1).grid(row=4, column=0, pady=10, padx=5)
    entry_edad = tk.Entry(root, font=("Arial", 15), width=15)
    entry_edad.grid(row=4, column=1, pady=10, padx=5)

    tk.Label(root, text="Género:", font=("Arial", 15), width=15, height=1).grid(row=4, column=0, pady=10, padx=5)
    entry_genero = tk.Entry(root, font=("Arial", 15), width=15)
    entry_genero.grid(row=5, column=1, pady=10, padx=5)

    tk.Button(root, text="Modificar Turista", command=modificar_turista, font=("Arial", 15), width=15, height=1).grid(row=6, column=1, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_turistas, font=("Arial", 15), width=15, height=1).grid(row=7, column=1, pady=10, padx=5)

def ventana_eliminar_turista():
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Turista")
    
    def eliminar_turista():
        id_turista = entry_id.get()

        resultado = Turista.Turista.eliminarTurista(id_turista=id_turista)
        if resultado:
                messagebox.showinfo("Error",".:: Turista Eliminado exitosamente ::..")
        else:
                messagebox.showerror("Error","...** No fue posible eliminar el turista, por favor intente nuevamente **...")
                
    tk.Label(root, text=" ..:: Eliminacion de Turistas ::..", font=("Arial", 15), width=20, height=1).pack(pady=10)

    tk.Label(root, text="ID Turista para Eliminar:", font=("Arial", 15), width=20, height=2).pack(pady=10)
    entry_id = tk.Entry(root,font=("Arial", 15), width=15)
    entry_id.pack(pady=10)

    tk.Button(root, text="Eliminar Turista", command=eliminar_turista,font=("Arial", 15), width=15, height=2).pack(pady=10)
    tk.Button(root, text="Volver al Menú", command=menu_turistas, font=("Arial", 15), width=15, height=2).pack(pady=10)

def ventana_mostrar_turista(): 
    borrarPantalla()
    root.geometry("1000x800")  
    root.title("Menú Turista")

    def mostrar_turistas():
        registro = Turista.Turista.mostrarTuristas()
    
        if registro:
            texto = ""
            for num, fila in enumerate(registro, 1):
                texto += f"Turista #{num}\nNombre: {fila[0]}.- Apellidos: {fila[1]}\nEdad: {fila[2]} Género: {fila[3]}\nEstancia: {fila[4]} ID: {fila[5]}\n\n"
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, texto)
        else:
            messagebox.showinfo("Información", "No hay turistas registrados.")


    
    text_area = tk.Text(root, height=10, width=80)
    text_area.pack(pady=10)

    tk.Button(root, text="Mostrar Turista", command=mostrar_turistas, font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Volver al Menú", command=menu_turistas, font=("Arial", 15), width=15, height=1).pack(pady=10)
    
    
#Codigo para tabla viajes
def ventana_crear_viaje():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Viaje")

    def crear_viaje():
        id_viaje = entry_id.get()
        destino = entry_destino.get()
        salida = entry_salida.get()
        costo = entry_costo.get()
        hora_partida = entry_hora_partida.get()
        estado_viaje = entry_estado_viaje.get()
        num_turistas = entry_num_turistas.get()

        obj_viaje = viajes.Viaje(id_viaje, destino, salida, float(costo), hora_partida, estado_viaje, num_turistas)
        resultado = obj_viaje.crearviaje()
        if resultado:
            print(f"\n \t \t..:: El Viaje fue registrado correctamente ::..")
        else:
            print(f"\n \t \t...** No fue posible registrar el viaje por favor verifique los datos e intente nuevamente **...")
            
    tk.Label(root, text=" ..:: Creacion de Viajes ::..", font=("Arial", 15), width=30, height=1).grid(row=0, column=1, pady=10)
    
    tk.Label(root, text="ID Viaje: ", font=("Arial", 15), width=15, height=1).grid(row=0, column=0, pady=10, padx=5)
    entry_id = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(root, text="Destino: ", font=("Arial", 15), width=15, height=1).grid(row=1, column=0, pady=10, padx=5)
    entry_destino = tk.Entry(root, font=("Arial", 15), width=15)
    entry_destino.grid(row=1, column=1, pady=10, padx=5)

    tk.Label(root, text="Salida(Formato: DD-MM-AA): ", font=("Arial", 15), width=20, height=1).grid(row=2, column=0, pady=10, padx=5)
    entry_salida = tk.Entry(root, font=("Arial", 15), width=15)
    entry_salida.grid(row=2, column=1, pady=10, padx=5)

    tk.Label(root, text="Costo del viaje: ", font=("Arial", 15), width=15, height=1).grid(row=3, column=0, pady=10, padx=5)
    entry_costo = tk.Entry(root, font=("Arial", 15), width=15)
    entry_costo.grid(row=3, column=1, pady=10, padx=5)

    tk.Label(root, text="Hora de Partida(Formato: HH:MM): ", font=("Arial", 15), width=20, height=1).grid(row=4, column=0, pady=10, padx=5)
    entry_hora_partida = tk.Entry(root,font=("Arial", 15), width=15)
    entry_hora_partida.grid(row=4, column=1, pady=10, padx=5)

    tk.Label(root, text="Estado del Viaje(Pendiente o Finalizado): ", font=("Arial", 15), width=20, height=1).grid(row=5, column=0, pady=10, padx=5)
    entry_estado_viaje = tk.Entry(root, font=("Arial", 15), width=15)
    entry_estado_viaje.grid(row=5, column=1, pady=10, padx=5)

    tk.Label(root, text="Numero de Turistas Permitidos: ", font=("Arial", 15), width=20, height=1).grid(row=6, column=0, pady=10, padx=5)
    entry_num_turistas = tk.Entry(root, font=("Arial", 15), width=15, height=1)
    entry_num_turistas.grid(row=6, column=1, pady=10, padx=5)

    tk.Button(root, text="Crear Viaje ", command=crear_viaje, font=("Arial", 15), width=15, height=1).grid(row=8, column=0, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_viajes, font=("Arial", 15), width=15, height=1).grid(row=8, column=1, pady=10, padx=5)

def ventana_eliminar_viaje():
    borrarPantalla()
    root.geometry("250x200")
    root.title("Menú Viaje")

    def eliminar_viaje():
        id_viaje = entry_id_viaje.get()
    
        if not id_viaje:
            messagebox.showwarning("Advertencia", "Debe ingresar el ID del viaje.")
            return
    
        resultado = viajes.Viaje.eliminarviaje(id_viaje)
    
        if resultado:
            messagebox.showinfo("Éxito", "Viaje eliminado exitosamente.")
        else:
            messagebox.showerror("Error", "No fue posible eliminar el viaje. Intente nuevamente.")
    
        tk.Label(root, text=" ..:: Eliminacion de Viajes ::..", font=("Arial", 15), width=30, height=1).pack(pady=10)


    tk.Label(root, text="ID del Viaje:", font=("Arial", 15), width=20, height=2).pack(pady=10)
    entry_id_viaje = tk.Entry(root,font=("Arial", 15), width=20,)
    entry_id_viaje.pack(pady=10)

    tk.Button(root, text="Eliminar Viaje", command=eliminar_viaje, font=("Arial", 15), width=30, height=1).pack(pady=10)
    tk.Button(root, text="Volver al Menú", command=menu_viajes, font=("Arial", 15), width=30, height=1).pack(pady=10)

def ventana_mostrar_viaje():
    borrarPantalla()
    root.geometry("600x400")
    root.title("Menú Viaje")
   
    def mostrar_viajes():
        registro = viajes.Viaje.mostrarviajes()
    
        if registro:
            text_area.delete(1.0, tk.END)
            texto = "Aquí están los Viajes registrados:\n"
            for num, fila in enumerate(registro, 1):
                texto += (f"Viaje #{num}\n"
                          f"ID: {fila[0]} - Destino: {fila[1]} - Salida: {fila[2]} - Costo: {fila[3]}\n"
                          f"Hora de Partida: {fila[4]} \n- Estado del Viaje: {fila[5]} - Número de Turistas: {fila[6]}\n\n")
            text_area.insert(tk.END, texto)
        else:
            messagebox.showinfo("Información", "No hay viajes registrados.")
    
    text_area = tk.Text(root, height=20, width=70)
    text_area.pack(pady=10)
    
    tk.Button(root, text="Mostrar Viajes", command=mostrar_viajes, font=("Arial", 15), width=30, height=1).pack(pady=10)
    tk.Button(root, text="Volver al Menú", command=menu_viajes, font=("Arial", 15), width=30, height=1).pack(pady=10)

#Inicio de codigo para tabla guias
def ventana_crear_guia():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Guia")

    def crear_guia():
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        edad = entry_edad.get()
        genero = entry_genero.get()
        experiencia = entry_experiencia.get()
        idioma = entry_idioma.get()
        tarifa = entry_tarifa.get()
        id_guia = entry_id_guia.get()
    
        if not (nombre and apellidos and edad and genero and experiencia and idioma and tarifa and id_guia):
           messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")
           return
    
        try:
            edad = int(edad)
            tarifa = float(tarifa)
        except ValueError:
            messagebox.showerror("Error", "Edad debe ser un número entero y tarifa debe ser un número decimal.")
            return
    
        obj_guia = guia.Guia(nombre, apellidos, edad, genero, experiencia, idioma, tarifa, id_guia)
        resultado = obj_guia.crearGuia()
    
        if resultado:
            messagebox.showinfo("Éxito", "Guía registrado correctamente.")
        else:
            messagebox.showerror("Error", "No fue posible registrar al Guía. Intente nuevamente.")
            
    tk.Label(root, text="Nombre:", font=("Arial", 15), width=15, height=1).grid(row=0, column=0, pady=10, padx=5)
    entry_nombre = tk.Entry(root, font=("Arial", 15), width=30)
    entry_nombre.grid(row=0, column=1, pady=10, padx=5)

    tk.Label(root, text="Apellidos:", font=("Arial", 15), width=15, height=1).grid(row=1, column=0, pady=10, padx=5)
    entry_apellidos = tk.Entry(root, font=("Arial", 15), width=30)
    entry_apellidos.grid(row=1, column=1, pady=10, padx=5)

    tk.Label(root, text="Edad:", font=("Arial", 15), width=15, height=1).grid(row=2, column=0, pady=10, padx=5)
    entry_edad = tk.Entry(root, font=("Arial", 15), width=15)
    entry_edad.grid(row=2, column=1, pady=10, padx=5)

    tk.Label(root, text="Género:", font=("Arial", 15), width=15, height=1).grid(row=3, column=0, pady=10, padx=5)
    entry_genero = tk.Entry(root, font=("Arial", 15), width=15)
    entry_genero.grid(row=3, column=1, pady=10, padx=5)

    tk.Label(root, text="Experiencia:", font=("Arial", 15), width=15, height=1).grid(row=4, column=0, pady=10, padx=5)
    entry_experiencia = tk.Entry(root, font=("Arial", 15), width=15, height=1)
    entry_experiencia.grid(row=4, column=1, pady=10, padx=5)

    tk.Label(root, text="Idioma:", font=("Arial", 15), width=15, height=1).grid(row=5, column=0, pady=10, padx=5)
    entry_idioma = tk.Entry(root, font=("Arial", 15), width=15)
    entry_idioma.grid(row=5, column=1, pady=10, padx=5)

    tk.Label(root, text="Tarifa:", font=("Arial", 15), width=15, height=1).grid(row=6, column=0, pady=10, padx=5)
    entry_tarifa = tk.Entry(root, font=("Arial", 15), width=15)
    entry_tarifa.grid(row=6, column=1, pady=10, padx=5)

    tk.Label(root, text="ID Guía:", font=("Arial", 15), width=15, height=1).grid(row=7, column=0, pady=10, padx=5)
    entry_id_guia = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id_guia.grid(row=7, column=1, pady=10, padx=5)

    tk.Button(root, text="Crear Guía", command=crear_guia, font=("Arial", 15), width=15, height=1).grid(row=3, column=3, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_guias, font=("Arial", 15), width=15, height=1).grid(row=4, column=3, pady=10, padx=5)

def ventana_modificar_guia():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Guia")
    
    def modificar_guia():
        id_guia = entry_id_guia.get()
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        edad = entry_edad.get()
        genero = entry_genero.get()
    
        if not (id_guia and nombre and apellidos and edad and genero):
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")
            return
        try:
            edad = int(edad)
            resultado = guia.Guia.actualizarGuia(nombre, apellidos, edad, genero, id_guia)
    
            if resultado:
                messagebox.showinfo("Éxito", "Datos del Guía modificados correctamente.")
            else:
                messagebox.showerror("Error", "No fue posible modificar la información. Intente nuevamente.")
        
        except ValueError:
            messagebox.showerror("Error", "Edad debe ser en número.")
        return

    tk.Label(root, text="ID del Guía a Modificar:", font=("Arial", 15), width=20, height=1).grid(row=1, column=0, pady=10, padx=5)
    entry_id_guia = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id_guia.grid(row=1, column=1, pady=10, padx=5)

    tk.Label(root, text="Nombre:", font=("Arial", 15), width=15, height=1).grid(row=2, column=0, pady=10, padx=5)
    entry_nombre = tk.Entry(root, font=("Arial", 15), width=15)
    entry_nombre.grid(row=2, column=1, pady=10, padx=5)

    tk.Label(root, text="Apellidos:", font=("Arial", 15), width=15, height=1).grid(row=3, column=0, pady=10, padx=5)
    entry_apellidos = tk.Entry(root, font=("Arial", 15), width=15)
    entry_apellidos.grid(row=2, column=1, pady=10, padx=5)

    tk.Label(root, text="Edad:", font=("Arial", 15), width=15, height=1).grid(row=4, column=0, pady=10, padx=5)
    entry_edad = tk.Entry(rootfont=("Arial", 15), width=15)
    entry_edad.grid(row=4, column=1, pady=10, padx=5)

    tk.Label(root, text="Género:", font=("Arial", 15), width=15, height=1).grid(row=5, column=0, pady=10, padx=5)
    entry_genero = tk.Entry(root, font=("Arial", 15), width=15)
    entry_genero.grid(row=5, column=1, pady=10, padx=5)

    tk.Button(root, text="Modificar Guía", command=modificar_guia, font=("Arial", 15), width=15, height=1).grid(row=6, column=1, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_guias, font=("Arial", 15), width=15, height=1).grid(row=7, column=1, pady=10, padx=5)
    
def ventana_eliminar_guia():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Guia")

    def eliminar_guia():
        id_guia = entry_id_guia.get()
    
        if not id_guia:
            messagebox.showwarning("Advertencia", "Debe ingresar el ID del Guía.")
            return
    
        resultado = guia.Guia.eliminarGuia(id_guia)
    
        if resultado:
            messagebox.showinfo("Éxito", "Guía eliminado exitosamente.")
        else:
            messagebox.showerror("Error", "No fue posible eliminar el Guía. Intente nuevamente.")

    tk.Label(root, text="ID Guía a Eliminar:").grid(row=1, column=0, pady=5, padx=5)
    entry_id_guia = tk.Entry(root)
    entry_id_guia.pack(pady=10)

    tk.Button(root, text="Eliminar Guía", command=eliminar_guia,font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Volver al Menú", command=menu_guias, font=("Arial", 15), width=15, height=1).pack(pady=10)

def ventana_mostrar_guia():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Guia")

    def mostrar_guias():
        registro = guia.Guia.mostrarGuias()
    
        if registro:
            text_area.delete(1.0, tk.END)
            texto = "Aquí están los Guías registrados:\n"
            for num, fila in enumerate(registro, 1):
                texto += (f"Guía #{num}\n"
                          f"Nombre: {fila[0]} - Apellidos: {fila[1]} - Edad: {fila[2]} - Género: {fila[3]}\n"
                          f"Experiencia: {fila[4]} - Idioma: {fila[5]} - Tarifa: {fila[6]} - ID: {fila[7]}\n\n")
            text_area.insert(tk.END, texto)
        else:
            messagebox.showinfo("Información", "No hay guías registrados.")
        
    text_area = tk.Text(root, height=15, width=80)
    text_area.pack(pady=10)
    
    tk.Button(root, text="Mostrar Guías", command=mostrar_guias, font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Volver al Menú", command=menu_guias, font=("Arial", 15), width=15, height=1).pack(pady=10)

#Codigo para tabla paseos
def ventana_crear_paseo():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Paseos")
    
    def crear_paseo():
        id_ruta = entry_id_ruta.get()
        tiempo = entry_tiempo.get()
        guia = entry_guia.get()
        estado_paseo = entry_estado.get()
        destino = entry_destino.get()
        costo = entry_costo.get()
        hora_partida = entry_hora_partida.get()
        
        obj_paseo = PaseoTuristico.PaseoTuristas(id_ruta, tiempo, guia, estado_paseo, destino, costo, hora_partida)
        resultado = obj_paseo.crearpaseo()
        
        if resultado:
            messagebox.showinfo("Éxito", "El paseo turístico fue registrado correctamente.")
        else:
            messagebox.showerror("Error", "No fue posible registrar el paseo, por favor verifique los datos e intente nuevamente.")

    tk.Label(root, text="ID de la Ruta:", font=("Arial", 15), width=15, height=1).grid(row=0, column=0, pady=10, padx=5)
    entry_id_ruta = tk.Entry(root, ont=("Arial", 15), width=15)
    entry_id_ruta.grid(row=0, column=1, pady=10, padx=5)

    tk.Label(root, text="Tiempo de Duración:", font=("Arial", 15), width=15, height=1).grid(row=1, column=0, pady=10, padx=5)
    entry_tiempo = tk.Entry(root, ont=("Arial", 15), width=15)
    entry_tiempo.grid(row=1, column=1, pady=10, padx=5)

    tk.Label(root, text="Guía:", font=("Arial", 15), width=15, height=1).grid(row=2, column=0, pady=10, padx=5)
    entry_guia = tk.Entry(root, font=("Arial", 15), width=15)
    entry_guia.grid(row=2, column=1, pady=10, padx=5)

    tk.Label(root, text="Estado del Paseo:", font=("Arial", 15), width=15, height=1).grid(row=3, column=0, pady=10, padx=5)
    entry_estado = tk.Entry(root, font=("Arial", 15), width=15)
    entry_estado.grid(row=3, column=1, pady=10, padx=5)

    tk.Label(root, text="Destino:", font=("Arial", 15), width=15, height=1).grid(row=4, column=0, pady=10, padx=5)
    entry_destino = tk.Entry(root, font=("Arial", 15), width=15)
    entry_destino.grid(row=4, column=1, pady=10, padx=5)

    tk.Label(root, text="Costo del Paseo:", font=("Arial", 15), width=15, height=1).grid(row=5, column=0, pady=10, padx=5)
    entry_costo = tk.Entry(root, font=("Arial", 15), width=15)
    entry_costo.grid(row=5, column=1, pady=10, padx=5)

    tk.Label(root, text="Hora de Partida (24 hrs):", font=("Arial", 15), width=15, height=1).grid(row=6, column=0, pady=10, padx=5)
    entry_hora_partida = tk.Entry(root, font=("Arial", 15), width=15)
    entry_hora_partida.grid(row=6, column=1, pady=10, padx=5)
    
    tk.Button(root, text="Crear Paseo", command=crear_paseo, font=("Arial", 15), width=15, height=1).grid(row=7, column=0, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_paseos, font=("Arial", 15), width=15, height=1).grid(row=7, column=1, pady=10, padx=5)

def ventana_eliminar_paseo():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Guia")

    def eliminar_paseo():
        id_ruta = entry_id_ruta.get()
        resultado = PaseoTuristico.PaseoTuristas.eliminarpaseo(id_ruta)
        
        if resultado:
            messagebox.showinfo("Éxito", "Paseo turístico eliminado exitosamente.")
        else:
            messagebox.showerror("Error", "No fue posible eliminar el paseo, por favor intente nuevamente.")
        
    tk.Label(root, text="ID de la Ruta:").pack(pady=10)
    entry_id_ruta = tk.Entry(root)
    entry_id_ruta.pack(pady=10)

    tk.Button(root, text="Eliminar Paseo", command=eliminar_paseo, font=("Arial", 15), width=15, height=1).pack(pady=10)
    tk.Button(root, text="Volver al Menú", command=menu_paseos, font=("Arial", 15), width=15, height=1).pack(pady=10)
    
def ventana_mostrar_paseos():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Paseos")

    def mostrar_paseos():
        registro = PaseoTuristico.PaseoTuristas.mostrarpaseos()
    
        if registro:
            texto = "Aquí están los paseos turísticos registrados:\n"
            for num, fila in enumerate(registro, 1):
                texto += (f"Paseo #{num}\n"
                          f"ID: {fila[0]} - Tiempo de Duración: {fila[1]} - Guía: {fila[2]}\n"
                          f"Estado del Paseo: {fila[3]} - Destino: {fila[4]} - Costo: {fila[5]}\n"
                          f"Hora de Partida: {fila[6]}\n\n")
            text_area.insert(tk.END, texto)
        else:
            messagebox.showinfo("Información", "No hay paseos turísticos registrados.")

    text_area = tk.Text(root, height=20, width=85)
    text_area.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
    
    tk.Button(root, text="Mostrar Paseos", command=mostrar_paseos,font=("Arial", 15), width=15, height=1).grid(row=1, column=0, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_paseos, font=("Arial", 15), width=15, height=1).grid(row=1, column=1, pady=10, padx=5)

#Codigo para tabla reservas
def ventana_reservar_viaje():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Reservas")

    def crear_reserva_viaje():
        id_viaje = entry_id_viaje.get()
        id_turista = entry_id_turista.get()
        obj_reserva = reservarViaje.ReservaViaje(id_viaje, id_turista)
        
        resultado = obj_reserva.crearReserva()
        
        if resultado:
            messagebox.showinfo("Éxito", "Reserva realizada correctamente.")
        else:
            messagebox.showerror("Error", "No fue posible realizar la reserva, por favor verifique los datos e intente nuevamente.")
        
    tk.Label(root, text="ID del Viaje:", font=("Arial", 15), width=15, height=1).grid(row=0, column=0, pady=10, padx=5)
    entry_id_viaje = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id_viaje.grid(row=0, column=1, pady=10, padx=5)

    tk.Label(root, text="ID del Turista:", font=("Arial", 15), width=15, height=1).grid(row=1, column=0, pady=10, padx=5)
    entry_id_turista = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id_turista.grid(row=1, column=1, pady=10, padx=5)

    tk.Button(root, text="Reservar Viaje", command=crear_reserva_viaje, font=("Arial", 15), width=15, height=1).grid(row=2, column=0, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_reservar, font=("Arial", 15), width=15, height=1).grid(row=2, column=1, pady=10, padx=5)

def ventana_reservar_paseo():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Reservas")

    def crear_reserva_paseo():
        id_ruta = entry_id_ruta.get()
        id_guia = entry_id_guia.get()
        id_turista = entry_id_turista.get()
        id_viaje = entry_id_viaje.get()
        
        obj_reserva = reservarPaseo.ReservaPaseo(id_ruta, id_guia, id_turista, id_viaje)
        resultado = obj_reserva.crearReserva()
        
        if resultado:
            messagebox.showinfo("Éxito", "Reserva realizada correctamente.")
        else:
            messagebox.showerror("Error", "No fue posible realizar la reserva, por favor verifique los datos e intente nuevamente.")
    
    tk.Label(root, text="ID de la Ruta:", font=("Arial", 15), width=15, height=1).grid(row=0, column=0, pady=10, padx=5)
    entry_id_ruta = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id_ruta.grid(row=0, column=1, pady=10, padx=5)

    tk.Label(root, text="ID del Guía:", font=("Arial", 15), width=15, height=1).grid(row=1, column=0, pady=10, padx=5)
    entry_id_guia = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id_guia.grid(row=1, column=1, pady=10, padx=5)

    tk.Label(root, text="ID del Turista:", font=("Arial", 15), width=15, height=1).grid(row=2, column=0, pady=10, padx=5)
    entry_id_turista = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id_turista.grid(row=2, column=1, pady=10, padx=5)

    tk.Label(root, text="ID del Viaje:", font=("Arial", 15), width=15, height=1).grid(row=3, column=0, pady=10, padx=5)
    entry_id_viaje = tk.Entry(root, font=("Arial", 15), width=15)
    entry_id_viaje.grid(row=3, column=1, pady=10, padx=5)

    tk.Button(root, text="Reservar Paseo", command=crear_reserva_paseo, font=("Arial", 15), width=15, height=1).grid(row=4, column=0, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_reservar, font=("Arial", 15), width=15, height=1).grid(row=4, column=1, pady=10, padx=5)

def ventana_eliminar_reserva_viaje():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Reservas")

    def eliminar_reserva_viaje():
        folio = entry_folio.get()
        resultado = reservarViaje.ReservaViaje.eliminarReserva(folio)
        
        if resultado:
            messagebox.showinfo("Éxito", "Reserva eliminada exitosamente.")
        else:
            messagebox.showerror("Error", "No fue posible eliminar la reserva, por favor intente nuevamente.")
        

    tk.Label(root, text="Folio de la Reserva:", font=("Arial", 15), width=15, height=1).grid(row=0, column=0, pady=10, padx=5)
    entry_folio = tk.Entry(root, font=("Arial", 15), width=15, height=1)
    entry_folio.grid(row=0, column=1, pady=10, padx=5)

    tk.Button(root, text="Reservar Paseo", command=eliminar_reserva_viaje, font=("Arial", 15), width=15, height=1).grid(row=1, column=0, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_reservar, font=("Arial", 15), width=15, height=1).grid(row=1, column=1, pady=10, padx=5)

def ventana_eliminar_reserva_paseo():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Reservas")

    def eliminar_reserva_paseo():
        folio = entry_folio.get()
        resultado = reservarPaseo.ReservaPaseo.eliminarReservas(folio)
        
        if resultado:
            messagebox.showinfo("Éxito", "Reserva eliminada exitosamente.")
        else:
            messagebox.showerror("Error", "No fue posible eliminar la reserva, por favor intente nuevamente.")
    
    tk.Label(root, text="Folio de la Reserva:", font=("Arial", 15), width=15, height=1).grid(row=0, column=0, pady=10, padx=5)
    entry_folio = tk.Entry(root, font=("Arial", 15), width=15)
    entry_folio.grid(row=0, column=1, pady=10, padx=5)

    tk.Button(root, text="Reservar Paseo", command=eliminar_reserva_paseo, font=("Arial", 15), width=15, height=1).grid(row=1, column=0, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_reservar, font=("Arial", 15), width=15, height=1).grid(row=1, column=1, pady=10, padx=5)

def ventana_mostrar_reserva_viaje():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Reservas")

    def mostrar_reservas_viaje():
        resultado = reservarViaje.ReservaViaje.mostrarReservas()
        if resultado:
            texto = "Aquí están las reservas de viaje registradas:\n"
            for num, fila in enumerate(resultado, 1):
                texto += (f"Reserva #{num}\n"
                          f"Folio: {fila[0]} - ID del Viaje: {fila[1]} - ID del Turista: {fila[2]}\n\n")
            text_area.insert(tk.END, texto)
        else:
            messagebox.showinfo("Información", "No hay reservas registradas.")

    text_area = tk.Text(root, height=20, width=80)
    text_area.grid(pady=10, padx=10)
    
    tk.Button(root, text="Mostrar Paseos", command=mostrar_reservas_viaje, font=("Arial", 15), width=15, height=1).grid(row=9, column=0, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_reservar, font=("Arial", 15), width=15, height=1).grid(row=10, column=0, pady=10)

def ventana_mostrar_reserva_paseo():
    borrarPantalla()
    root.geometry("1000x800")
    root.title("Menú Reservas")

    def mostrar_reservas_paseo():
        resultado = reservarPaseo.ReservaPaseo.mostrarReservas()
    
        if resultado:
            texto = "Aquí están las reservas de paseo registradas:\n"
            for num, fila in enumerate(resultado, 1):
                texto += (f"Reserva #{num}\n"
                          f"Folio: {fila[0]} - ID de la Ruta: {fila[1]} - ID del Guía: {fila[2]} - ID del Turista: {fila[3]} - ID del Viaje: {fila[4]}\n\n")
            text_area.insert(tk.END, texto)
        else:
            messagebox.showinfo("Información", "No hay reservas registradas.")

    text_area = tk.Text(root, height=20, width=80)
    text_area.grid(row=8, pady=10, padx=10)
    
    tk.Button(root, text="Mostrar Paseos", command=mostrar_reservas_paseo, font=("Arial", 15), width=15, height=1).grid(row=9, column=0, pady=10, padx=5)
    tk.Button(root, text="Volver al Menú", command=menu_reservar, font=("Arial", 15), width=15, height=1).grid(row=9, column=0, pady=10, padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    menu_inicio()
    root.mainloop()
