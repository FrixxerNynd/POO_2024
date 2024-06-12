#5.- 
#Crear una lista y un diccionario con el contenido de esta tabla: 

#  ACCION              TERROR        DEPORTES
#  MAXIMA VELOCIDAD    LA MONJA       ESPN
#  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#  RAPIDO Y FURIOSO I  LA MALDICION   ACCION

#  imprimir la información

lista_peliculas = [
    ["ACCION","TERROR","DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

print("Lista de películas:")
for pelicula in lista_peliculas:
    print(pelicula)

diccionario_peliculas = {
    "pelicula1": {"accion": "MAXIMA VELOCIDAD", "terror": "LA MONJA", "deportes": "ESPN"},
    "pelicula2": {"accion": "ARMA MORTAL 4", "terror": "EL CONJURO", "deportes": "MAS DEPORTE"},
    "pelicula3": {"accion": "RAPIDO Y FURIOSO I", "terror": "LA MALDICION", "deportes": "ACCION"}
}


print("\nDiccionario de películas:")
for key, value in diccionario_peliculas.items():
    print(f"{key}: {value}")