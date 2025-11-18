"""Funciones para agrupar y mostrar categorías anidadas."""

from __future__ import annotations

from typing import Any

from utils import formatear_monto


def nuevo_nodo_categoria() -> dict[str, Any]:
    return {"movimientos": [], "hijos": {}, "totales": {"Ingreso": 0.0, "Gasto": 0.0}}


def insertar_categoria(node: dict[str, Any], partes: list[str], mov: dict[str, Any]) -> None:
    tipo = mov.get("tipo")
    monto = mov.get("monto", 0.0)
    if tipo in node["totales"]:
        node["totales"][tipo] += monto
    if not partes:
        node["movimientos"].append(mov)
        return
    cabeza, *resto = partes
    hijos = node["hijos"]
    if cabeza not in hijos:
        hijos[cabeza] = nuevo_nodo_categoria()
    insertar_categoria(hijos[cabeza], resto, mov)


def imprimir_arbol_por_tipo(nombre: str, nodo: dict[str, Any], tipo: str, nivel: int) -> bool:
    total = nodo["totales"].get(tipo, 0.0)
    if total <= 0:
        return False

    indent = "  " * nivel
    print(f"{indent}- {nombre}: {formatear_monto(total)}")

    for hijo in sorted(nodo["hijos"]):
        imprimir_arbol_por_tipo(hijo, nodo["hijos"][hijo], tipo, nivel + 1)

    return True


def listar_categorias(movimientos: list[dict[str, Any]]) -> None:
    """Muestra las categorías anidadas separando ingresos y gastos."""
    if not movimientos:
        print("No hay movimientos para agrupar por categorias.")
        return

    raiz = nuevo_nodo_categoria()
    for mov in movimientos:
        categoria = mov.get("categoria") or "Sin categoria"
        partes = [p.strip() for p in categoria.split("/") if p.strip()]
        if not partes:
            partes = ["Sin categoria"]
        insertar_categoria(raiz, partes, mov)

    print("\nCategorias de ingresos:")
    hay_ingresos = False
    for nombre in sorted(raiz["hijos"]):
        if imprimir_arbol_por_tipo(nombre, raiz["hijos"][nombre], "Ingreso", 0):
            hay_ingresos = True
    if not hay_ingresos:
        print("  (sin ingresos)")

    print("\nCategorias de gastos:")
    hay_gastos = False
    for nombre in sorted(raiz["hijos"]):
        if imprimir_arbol_por_tipo(nombre, raiz["hijos"][nombre], "Gasto", 0):
            hay_gastos = True
    if not hay_gastos:
        print("  (sin gastos)")
