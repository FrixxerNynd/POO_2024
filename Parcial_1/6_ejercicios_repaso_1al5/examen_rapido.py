
n = 0
promedio_total = 0
while True:
    Alumno = input("Ingrese el nombre del alumno: \n")
    Carrera = input("Ingrese la carrera cursada por el alumno: \n")
    Calificacion1 = int(input("Ingrese la calificacion del primer parcial: \n"))
    Calificacion2 = int(input("Ingrese la calificacion del segundo parcial: \n"))
    Calificacion3 = int(input("Ingrese la calificacion del tercer parcial: \n"))
    Calif_proyecto = int(input("Ingrese la calificacion del proyecto final: \n"))


    promedio = (Calificacion1 + Calificacion2 + Calificacion3) / 3


    print(f"Calificacion final del alumno: {Alumno} de la carrera de: {Carrera}")
    Calificacion_final = (promedio + Calif_proyecto) /2

    if Calificacion_final < 80 and Calif_proyecto >50:
        print("El Alumno presenta examen extraordinario")

    n = n + 1
    promedio_total = (promedio_total + Calificacion_final) / n

    Respuesta = input("¿Deseas realizar otra captura (Si/No)? \n")
    if Respuesta =="Si" or Respuesta == "si":
        continue
    else:
        break
print(f"El promedio de la calificacion final todos los alumnos es: {promedio_total}")