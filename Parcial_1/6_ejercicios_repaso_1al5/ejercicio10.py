#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

calificaciones = []

for i in range(1, 16):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
    calificaciones.append(calificacion)


aprobados = sum(1 for calificacion in calificaciones if calificacion >= 80)
no_aprobados = 15 - aprobados


print(f"Total de alumnos: {len(calificaciones)}")
print(f"Aprobados: {aprobados}")
print(f"No Aprobados: {no_aprobados}")
