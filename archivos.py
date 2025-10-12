"""
Módulo de manejo de archivos para el Gestor de Gastos
Contiene funciones para cargar y guardar datos en JSON
"""

import json
import os

# Variable global para el archivo de datos
ARCHIVO_DATOS = "movimientos.json"

def cargar_datos():
    """Carga los movimientos desde el archivo JSON si existe"""
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as archivo:
                movimientos = json.load(archivo)
            print(f"Se cargaron {len(movimientos)} movimientos desde el archivo.")
            return movimientos
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error al cargar datos: {e}")
            return []
    else:
        print("No se encontró archivo de datos previo. Iniciando con lista vacía.")
        return []

def guardar_datos(movimientos):
    """Guarda los movimientos actuales en el archivo JSON"""
    try:
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as archivo:
            json.dump(movimientos, archivo, indent=2, ensure_ascii=False)
        print(f"Datos guardados correctamente ({len(movimientos)} movimientos).")
    except IOError as e:
        print(f"Error al guardar datos: {e}")

def borrar_archivo_datos():
    """Elimina el archivo de datos del disco"""
    try:
        if os.path.exists(ARCHIVO_DATOS):
            os.remove(ARCHIVO_DATOS)
            print("Archivo de datos eliminado.")
    except OSError as e:
        print(f"Error al eliminar archivo: {e}")