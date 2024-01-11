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

# Load the list of generos
lista_generos = load_generos_json()

# Create a new generos
def crear_generos():
    limpiar_pantalla()
    print("----------- Crear Genero -----------")
    numero_id = no_vacio("Ingrese la ID del Genero: ")
    nombre = solo_letras("Ingrese el Nombre del Genero: ")  

    # Create a genero dictionary
    genero = {
        "id": numero_id,
        "nombre": nombre,
    }
    
    # Add the new genero to the list
    lista_generos.append(genero)
    print("Se creó el genero con éxito\n")
    guardar_json()


# Save the list of generos to the JSON file
def guardar_json():
    try:
      with open(os.path.join("data", "generos.json"), 'w') as archivo_json:
        # Save the list of generos to the JSON file
        json.dump(lista_generos, archivo_json, indent=2)
        print("La lista de generos ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya generos guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
      
# Display the list of generos
def listar_generos():
    limpiar_pantalla()
    print("----------- Listar Generos -----------")
    for index, genero in enumerate(lista_generos, start=1):
        print(f"{index}. ID: {genero['id']}, Nombre: {genero['nombre']}")