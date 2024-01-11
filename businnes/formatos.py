import json
import os
from commons.utils import *

def load_formatos_json():
    try:
        with open(os.path.join("data", "formatos.json"), 'r') as archivo_json:        
            lista_formatos = json.load(archivo_json)
            print("La lista de formatos ha sido guardada")
            return lista_formatos
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

lista_formatos = load_formatos_json()


def crear_formatos():
    limpiar_pantalla()
    print("----------- Crear Formatos -----------")
    numero_id = no_vacio("Ingrese la ID del formato: ")
    nombre = solo_letras("Ingrese el nombre del formato: ")

    formato = {
        "id": numero_id,
        "nombre": nombre
    }
    
    lista_formatos.append(formato)
    print("Se creó el formato con éxito\n")
    guardar_json_formatos()
    

def guardar_json_formatos():
    try:
      with open(os.path.join("data", "formatos.json"), 'w') as archivo_json:
        json.dump(lista_formatos, archivo_json, indent=2)
        print("La lista de Formatos ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya formatos guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
        


def listar_formatos():
    # Mostrar la lista de formatos
    limpiar_pantalla()
    print("----------- Listar Formatos -----------")
    for index, formato in enumerate(lista_formatos, start=1):
        print(f"{index}. ID: {formato['id']}, Nombre: {formato['nombre']}")