"""Funciones de validación para entradas de texto y montos."""

MIN_CATEGORIA = 3
MIN_DESCRIPCION = 3

def normalizar_texto(valor: str | None) -> str:
    return (valor or "").strip()

def validar_monto(valor: str):
    """Valida un monto numérico positivo a partir de la entrada del usuario."""
    try:
        monto = float(valor)
    except (TypeError, ValueError):
        return None, "Por favor ingresa un monto válido."

    if monto <= 0:
        return None, "El monto debe ser mayor a 0."

    return monto, None

def validar_texto(valor: str | None, minimo: int, nombre: str):
    """Valida que el texto tenga longitud mínima."""
    texto = normalizar_texto(valor)

    if not texto:
        return None, f"{nombre} no puede estar vacío/a."

    if len(texto) < minimo:
        return None, f"{nombre} debe tener al menos {minimo} caracteres."

    return texto, None

def validar_categoria(valor: str | None):
    return validar_texto(valor, MIN_CATEGORIA, "La categoría")

def validar_descripcion(valor: str | None):
    return validar_texto(valor, MIN_DESCRIPCION, "La descripción")
