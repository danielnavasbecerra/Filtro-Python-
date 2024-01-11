import json
import os
from commons.utils import *

# Load generos data from JSON file
def load_generos_json():
    try:
        with open(os.path.join("data", "generos.json"), 'r') as archivo_json:        
            # Load generos data from JSON file
            lista_generos = json.load(archivo_json)
            print("La lista de generos ha sido guardada")
            return lista_generos
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def load_peliculas_json():
    try:
        with open(os.path.join("data", "peliculas.json"), 'r') as archivo_json:        
            lista_peliculas = json.load(archivo_json)
            print("La lista de peliculas ha sido guardada")
            return lista_peliculas
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def load_actores_json():
    try:
        with open(os.path.join("data", "actores.json"), 'r') as archivo_json:        
            lista_actores = json.load(archivo_json)
            print("La lista de actores ha sido guardada")
            return lista_actores
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# Load the list of generos
lista_generos = load_generos_json()
lista_peliculas = load_peliculas_json()
lista_actores = load_actores_json()


def listar_pelicula_genero_especifico():
    limpiar_pantalla()
    print("-------- Listar Pelicula Genero Especifico --------")
    for index, genero in enumerate(lista_generos, start=1):
        print(f"{index}. ID: {genero['id']}, Nombre: {genero['nombre']}")
    id_genero = input("Ingrese el ID del Genero que desea listar: ")

    # Buscar la película en la lista por su ID
    genero_encontrado = None
    for genero in lista_generos:
        if genero["id"] == id_genero:
            genero_encontrado = genero
            break
    else:
        print(f"No se encontró ningun genero con el ID {id_genero}.")

    for pelicula in lista_peliculas:
        if pelicula['generos'] == genero_encontrado:
        # Mostrar información de la película
            print(f"\nInformacion de peliculas con el genero {genero_encontrado['nombre']}:")
            print(f"ID: {pelicula['id']}")
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Duración: {pelicula['duracion']}")
            print(f"Sinopsis: {pelicula['sinopsis']}")
            print(f"Géneros: {pelicula['generos']['nombre']}")
            print(f"Actores: {pelicula['actores']['nombre']}")
            print(f"Formato: {pelicula['formato']['nombre']}")
        else:
            print("No se encontro ninguna pelicula con ese genero")
    


def listar_pelicula_actor_especifico():
    limpiar_pantalla()
    print("-------- Listar Pelicula Actor Especifico --------")
    for index, actor in enumerate(lista_actores, start=1):
        print(f"{index}. ID: {actor['id']}, Nombre: {actor['nombre']}")
    id_actor = input("Ingrese el ID del Actor que desea listar: ")

    # Buscar la película en la lista por su ID
    actor_encontrado = None
    for actor in lista_actores:
        if actor["id"] == id_actor:
            actor_encontrado = actor
            break
    else:
        print(f"No se encontró ningun genero con el ID {id_actor}.")

    for pelicula in lista_peliculas:
        if pelicula['actores'] == actor_encontrado:
        # Mostrar información de la película
            print(f"\nInformacion de peliculas con el actor {actor_encontrado['nombre']}:")
            print(f"ID: {pelicula['id']}")
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Duración: {pelicula['duracion']}")
            print(f"Sinopsis: {pelicula['sinopsis']}")
            print(f"Géneros: {pelicula['generos']['nombre']}")
            print(f"Actores: {pelicula['actores']['nombre']}")
            print(f"Formato: {pelicula['formato']['nombre']}")
        else:
            print("No se encontro ninguna pelicula que tenga a ese actor")
    


def buscar_pelicula_mostrando_sinopsis_actores():
    limpiar_pantalla()
    print("------ Buscar Pelicula Mostrando (Sinopsis, Actores) ------")
    for index, pelicula in enumerate(lista_peliculas, start=1):
        print(f"""{index}.  ID: {pelicula['id']}
                Nombre: {pelicula['nombre']}
                Duracion: {pelicula['duracion']}
                Sinopsis: {pelicula['sinopsis']}
                Géneros: {pelicula['generos']['nombre']}
                Actores: {pelicula['actores']['nombre']}
                Formato: {pelicula['formato']['nombre']}""")
        print("----------------------------------------")
    id_pelicula = input("Ingrese el ID de la pelicula que desea Buscar: ")

    # Buscar la película en la lista por su ID
    pelicula_encontrada = None
    for pelicula in lista_peliculas:
        if pelicula["id"] == id_pelicula:
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada:
        # Mostrar información de la película
        print("\nInformacion de la pelicula")
        print(f"ID: {pelicula_encontrada['id']}")
        print(f"Nombre: {pelicula_encontrada['nombre']}")
        print(f"Sinopsis: {pelicula_encontrada['sinopsis']}")
        print(f"Actores: {pelicula_encontrada['actores']['nombre']}")
    else:
        print(f"No se encontró ninguna película con el ID {id_pelicula}.")