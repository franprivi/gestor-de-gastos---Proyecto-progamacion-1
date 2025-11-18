"""Funciones de persistencia para el Gestor de Gastos."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
ARCHIVO_DATOS = DATA_DIR / "movimientos.json"


def asegurar_directorio() -> None:
    """Garantiza que el directorio de datos exista."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def cargar_datos() -> list[dict[str, Any]]:
    """Carga los movimientos desde el archivo JSON si existe."""
    asegurar_directorio()

    if not ARCHIVO_DATOS.exists():
        print("No se encontró archivo de datos previo. Iniciando con lista vacía.")
        return []

    try:
        with ARCHIVO_DATOS.open("r", encoding="utf-8") as archivo:
            movimientos = json.load(archivo)
        print(f"Se cargaron {len(movimientos)} movimientos desde el archivo.")
        return movimientos
    except (json.JSONDecodeError, OSError) as error:
        print(f"Error al cargar datos: {error}")
        return []


def guardar_datos(movimientos: list[dict[str, Any]]) -> None:
    """Guarda los movimientos actuales en el archivo JSON."""
    try:
        asegurar_directorio()
        with ARCHIVO_DATOS.open("w", encoding="utf-8") as archivo:
            json.dump(movimientos, archivo, indent=2, ensure_ascii=False)
        print(f"Datos guardados correctamente ({len(movimientos)} movimientos).")
    except OSError as error:
        print(f"Error al guardar datos: {error}")


def borrar_archivo_datos() -> None:
    """Elimina el archivo de datos del disco."""
    try:
        if ARCHIVO_DATOS.exists():
            ARCHIVO_DATOS.unlink()
            print("Archivo de datos eliminado.")
    except OSError as error:
        print(f"Error al eliminar archivo: {error}")