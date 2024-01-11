import json
import os
from commons.utils import *
from commons.menus import menu_modificar_peliculas

def load_peliculas_json():
    try:
        with open(os.path.join("data", "peliculas.json"), 'r') as archivo_json:        
            lista_peliculas = json.load(archivo_json)
            print("La lista de peliculas ha sido guardada")
            return lista_peliculas
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def load_generos_json():
    try:
        with open(os.path.join("data", "generos.json"), 'r') as archivo_json:        
            # Load generos data from JSON file
            lista_generos = json.load(archivo_json)
            print("La lista de generos ha sido guardada")
            return lista_generos
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

def load_formatos_json():
    try:
        with open(os.path.join("data", "formatos.json"), 'r') as archivo_json:        
            lista_formatos = json.load(archivo_json)
            print("La lista de formatos ha sido guardada")
            return lista_formatos
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# Load the list
lista_peliculas = load_peliculas_json()
lista_generos = load_generos_json()
lista_actores = load_actores_json()
lista_formatos = load_formatos_json()


def agregar_peliculas():
    limpiar_pantalla()
    print("----------- Agregar Peliculas -----------")
    numero_id = no_vacio("Ingrese la ID de la pelicula: ")
    nombre = no_vacio("Ingrese el nombre de la pelicula: ")
    duracion = no_vacio("Ingrese la duracion de la pelicula: ")
    sinopsis = no_vacio("Ingrese la sinopsis de la pelicula: ")
    generos = seleccione_genero("Ingrese el ID del genero que desea agregar a la Pelicula: ")
    actores = seleccione_actor("Ingrese el ID del actor que desea agregar a la Pelicula: ")
    formato = seleccione_formato("Ingrese el ID del formato que desea agregar a la Pelicula: ")

    pelicula = {
        "id": numero_id,
        "nombre": nombre,
        "duracion": duracion,
        "sinopsis": sinopsis,
        "generos": generos,
        "actores": actores,
        "formato": formato
    }

    lista_peliculas.append(pelicula)
    print("Se creó la pelicula con éxito\n")
    guardar_json_peliculas()
    

def guardar_json_peliculas():
    try:
      with open(os.path.join("data", "peliculas.json"), 'w') as archivo_json:
        json.dump(lista_peliculas, archivo_json, indent=2)
        print("La lista de Peliculas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya peliculas guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
        

def editar_pelicula():
    # Modify camper information
    limpiar_pantalla()
    print("----------- Editar Pelicula -----------")
    print("Lista Peliculas:")
    for index, pelicula in enumerate(lista_peliculas, start=1):
        print(f"""{index}.  ID: {pelicula['id']}
                Nombre: {pelicula['nombre']}
                Duracion: {pelicula['duracion']}
                Sinopsis: {pelicula['sinopsis']}
                Géneros: {pelicula['generos']['nombre']}
                Actores: {pelicula['actores']['nombre']}
                Formato: {pelicula['formato']['nombre']}""")
        print("----------------------------------------")
    buscar_id = no_vacio("Ingrese el ID de la Pelicula que desea modificar: ")
    encontrado = False
    for pelicula in lista_peliculas:
        if pelicula["id"] == buscar_id:
            print("\nDatos de la Pelicula:")
            print(f"ID: {pelicula['id']}")
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Duracion: {pelicula['duracion']}")
            print(f"Sinopsis: {pelicula['sinopsis']}")
            print(f"Géneros: {pelicula['generos']['nombre']}")
            print(f"Actores: {pelicula['actores']['nombre']}")
            print(f"Formato: {pelicula['formato']['nombre']}")
            encontrado = True
            
            op = menu_modificar_peliculas()
            if op==1:
                pelicula['id'] = no_vacio("Ingrese un nuevo ID: ")
                print("Modificacion exitosa")
                guardar_json_peliculas()
                break
            elif op==2:
                pelicula['nombre'] = no_vacio("Ingrese un nuevo Nombre: ")
                print("Modificacion exitosa")
                guardar_json_peliculas()
                break
            elif op==3:
                pelicula['duracion'] = no_vacio("Ingrese una nueva Duracion: ")
                print("Modificacion exitosa")
                guardar_json_peliculas()
                break
            elif op==4:
                pelicula['sinopsis'] = no_vacio("Ingrese una nueva Sinopsis: ")
                print("Modificacion exitosa")
                guardar_json_peliculas()
                break
            elif op==5:
                pelicula['generos'] = seleccione_genero("Ingrese un nuevo Genero: ")
                print("Modificacion exitosa")
                guardar_json_peliculas()
                break
            elif op==6:
                pelicula['actores'] = seleccione_actor("Ingrese un nuevo Actor: ")
                print("Modificacion exitosa")
                guardar_json_peliculas()
                break
            elif op==7:
                pelicula['formato'] = seleccione_formato("Ingrese un nuevo Formato: ")
                print("Modificacion exitosa")
                guardar_json_peliculas()
                break
            elif op==8:
                print("Regresando...")        
    if not encontrado:
        print(f"No se encontró una Pelicula con ID {buscar_id}.")


def eliminar_pelicula():
    limpiar_pantalla()
    print("----------- Eliminar Pelicula -----------")
    print("Lista Peliculas:")
    for index, pelicula in enumerate(lista_peliculas, start=1):
        print(f"{index}.  ID: {pelicula['id']}, Nombre: {pelicula['nombre']}")
        print("----------------------------------------")
    id_pelicula = input("Ingrese el ID de la película que desea eliminar: ")

    # Buscar la película en la lista por su ID (Este buscador es mas eficiente que los anteriores usados ;v)
    pelicula_encontrada = None
    for pelicula in lista_peliculas:
        if pelicula["id"] == id_pelicula:
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada:
        # Mostrar información de la película antes de eliminarla
        print("\nInformacion de la pelicula a eliminar:")
        print(f"ID: {pelicula_encontrada['id']}")
        print(f"Nombre: {pelicula_encontrada['nombre']}")
        print(f"Duración: {pelicula_encontrada['duracion']}")
        print(f"Sinopsis: {pelicula_encontrada['sinopsis']}")
        print(f"Géneros: {pelicula_encontrada['generos']['nombre']}")
        print(f"Actores: {pelicula_encontrada['actores']['nombre']}")
        print(f"Formato: {pelicula_encontrada['formato']['nombre']}")

        confirmacion = input("\n¿Está seguro de que desea eliminar esta película? (S/N): ").lower()
        if confirmacion == 's':
            # Eliminar la película de la lista
            lista_peliculas.remove(pelicula_encontrada)
            print("Película eliminada con éxito.")
            guardar_json_peliculas()
        elif confirmacion == 'n':
            print("Operación cancelada.")
        else:
            print("Error! Ingrese (S/N).")
    else:
        print(f"No se encontró ninguna película con el ID {id_pelicula}.")


def eliminar_actor():
    limpiar_pantalla()
    print("Lista Actores:")
    print("----------- Eliminar Actor -----------")
    for index, actor in enumerate(lista_actores, start=1):
        print(f"{index}. ID: {actor['id']}, Nombre: {actor['nombre']}")
    id_actor = input("Ingrese el ID del actor que desea eliminar: ")

    # Buscar el actor en la lista por su ID
    actor_encontrado = None
    for actor in lista_actores:
        if actor["id"] == id_actor:
            actor_encontrado = actor
            break

    if actor_encontrado:
        # Mostrar información del actor antes de eliminarlo
        print("\nInformación del actor a eliminar:")
        print(f"ID: {actor_encontrado['id']}")
        print(f"Nombre: {actor_encontrado['nombre']}")

        confirmacion = input("\n¿Está seguro de que desea eliminar este actor? (S/N): ").lower()
        if confirmacion == 's':
            # Eliminar el actor de la lista
            lista_actores.remove(actor_encontrado)
            print("Actor eliminado con éxito.")
            guardar_json_actores()
        elif confirmacion == 'n':
            print("Operación cancelada.")
        else:
            print("Error! Ingrese (S/N).")
    else:
        print(f"No se encontró ningún actor con el ID {id_actor}.")


def buscar_pelicula():
    limpiar_pantalla()
    print("----------- Buscar Pelicula -----------")
    id_pelicula = input("Ingrese el ID de la pelicula que desea Buscar: ")

    # Buscar la película en la lista por su ID
    pelicula_encontrada = None
    for pelicula in lista_peliculas:
        if pelicula["id"] == id_pelicula:
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada:
        # Mostrar información de la película
        print("\nInformacion de la pelicula buscada:")
        print(f"ID: {pelicula_encontrada['id']}")
        print(f"Nombre: {pelicula_encontrada['nombre']}")
        print(f"Duración: {pelicula_encontrada['duracion']}")
        print(f"Sinopsis: {pelicula_encontrada['sinopsis']}")
        print(f"Géneros: {pelicula_encontrada['generos']['nombre']}")
        print(f"Actores: {pelicula_encontrada['actores']['nombre']}")
        print(f"Formato: {pelicula_encontrada['formato']['nombre']}")
    else:
        print(f"No se encontró ninguna película con el ID {id_pelicula}.")


def listar_peliculas():
    # Mostrar la lista de Peliculas
    limpiar_pantalla()
    print("----------- Listar Peliculas -----------")
    for index, pelicula in enumerate(lista_peliculas, start=1):
        print(f"""{index}.  ID: {pelicula['id']}
                Nombre: {pelicula['nombre']}
                Duracion: {pelicula['duracion']}
                Sinopsis: {pelicula['sinopsis']}
                Géneros: {pelicula['generos']['nombre']}
                Actores: {pelicula['actores']['nombre']}
                Formato: {pelicula['formato']['nombre']}""")
        print("----------------------------------------")


def seleccione_genero(mensaje):
    print("Lista de Generos Registrados:")
    for index, genero in enumerate(lista_generos, start=1):
        print(f"{index}. ID: {genero['id']}, Nombre: {genero['nombre']}")

    # Solicitar el ID del genero al que se le registrará la pelicula
    id_genero = no_vacio(mensaje)

    # Buscar el genero en la base de datos
    encontrado = False
    for genero in lista_generos:
        if genero["id"] == id_genero:
            encontrado = True
            return genero
    if not encontrado:
        print("Genero no está Registrado")


def seleccione_actor(mensaje):
    print("Lista de Actores Registrados:")
    for index, actor in enumerate(lista_actores, start=1):
        print(f"{index}. ID: {actor['id']}, Nombre: {actor['nombre']}")

    id_actor = no_vacio(mensaje)

    encontrado = False
    for actor in lista_actores:
        if actor["id"] == id_actor:
            encontrado = True
            return actor
    if not encontrado:
        print("Genero no está Registrado")


def seleccione_formato(mensaje):
    print("Lista de Formatos Registrados:")
    for index, formato in enumerate(lista_formatos, start=1):
        print(f"{index}. ID: {formato['id']}, Nombre: {formato['nombre']}")

    id_formato = no_vacio(mensaje)

    encontrado = False
    for formato in lista_formatos:
        if formato["id"] == id_formato:
            encontrado = True
            return formato
    if not encontrado:
        print("Genero no está Registrado")


def guardar_json_actores():
    try:
      with open(os.path.join("data", "actores.json"), 'w') as archivo_json:
        json.dump(lista_actores, archivo_json, indent=2)
        print("La lista de Actores ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya actores guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")