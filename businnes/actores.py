import json
import os
from commons.utils import *

def load_actores_json():
    try:
        with open(os.path.join("data", "actores.json"), 'r') as archivo_json:        
            lista_actores = json.load(archivo_json)
            print("La lista de actores ha sido guardada")
            return lista_actores
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

lista_actores = load_actores_json()

# contador_actores = max(actor['ID'] for actor in lista_actores) if lista_actores else 0

def crear_actores():
    limpiar_pantalla()
    print("----------- Crear Actores -----------")
    numero_id = no_vacio("Ingrese la ID del actor: ")
    nombre = solo_letras("Ingrese el nombre del actor: ")
    
    # global contador_trainer
    # contador_trainer += 1

    actor = {
        "id": numero_id,
        "nombre": nombre
    }
    
    lista_actores.append(actor)
    print("Se creó el Actor con éxito\n")
    guardar_json_actores()
    

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
        


def listar_actores():
    # Mostrar la lista de actores
    limpiar_pantalla()
    print("----------- Listar Actores -----------")
    for index, actor in enumerate(lista_actores, start=1):
        print(f"{index}. ID: {actor['id']}, Nombre: {actor['nombre']}")