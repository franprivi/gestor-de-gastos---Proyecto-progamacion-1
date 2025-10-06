import json
import os

movimientos = []
ARCHIVO_DATOS = "movimientos.json"

def formatear_monto(monto):
    """Formatea el monto con formato de argentina, ejemplo: $1.541.200,23"""
    return f"${monto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def cargar_datos():
    """Carga los movimientos desde el archivo JSON si existe"""
    global movimientos
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as archivo:
                movimientos = json.load(archivo)
            print(f"Se cargaron {len(movimientos)} movimientos desde el archivo.")
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error al cargar datos: {e}")
            movimientos = []
    else:
        print("No se encontró archivo de datos previo. Iniciando con lista vacía.")

def guardar_datos():
    """Guarda los movimientos actuales en el archivo JSON"""
    try:
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as archivo:
            json.dump(movimientos, archivo, indent=2, ensure_ascii=False)
        print(f"Datos guardados correctamente ({len(movimientos)} movimientos).")
    except IOError as e:
        print(f"Error al guardar datos: {e}")

def borrar_todos_movimientos():
    """Borra todos los movimientos de la memoria y del archivo"""
    global movimientos
    try:
        confirmacion = input("¿Estás seguro de que quieres borrar TODOS los movimientos? (s/N): ").lower()
        if confirmacion == 's' or confirmacion == 'si':
            movimientos = []
            if os.path.exists(ARCHIVO_DATOS):
                os.remove(ARCHIVO_DATOS)
                print("Archivo de datos eliminado.")
            print("Todos los movimientos han sido borrados.")
        else:
            print("Operación cancelada.")
    except OSError as e:
        print(f"Error al eliminar archivo: {e}")

def menu():
    print("=== Menú Principal ===")
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Ver balance")
    print("4. Listar movimientos")
    print("5. Borrar todos los movimientos")
    print("6. Salir")
    
    try:
        opcion = int(input("Selecciona una opción (1 a 6): "))
        return opcion
    except ValueError:
        print("Error: Por favor ingresa un número válido entre 1 y 6.")
        return None

def registrar_ingreso():
    try:
        monto = float(input("Ingresa el monto del ingreso: "))
        categoria = input("Ingresa una categoría para el ingreso: ")
        descripcion = input("Ingresa una descripción para el ingreso: ")
        tipo = "Ingreso"
        movimientos.append({"tipo": tipo , "monto": monto, "categoria": categoria, "descripcion": descripcion}) 
        print(f"{tipo}  registrado correctamente.") 
        guardar_datos()  # Guardado automático
    except ValueError:
        print("Error: Por favor ingresa un monto válido.")

def registrar_gasto():
    try:
        monto = float(input("Ingresa el monto del gasto: "))
        categoria = input("Ingresa una categoría para el gasto: ")
        descripcion = input("Ingresa una descripción para el gasto: ")
        tipo = "Gasto"
        movimientos.append({"tipo": tipo , "monto": monto, "categoria": categoria, "descripcion": descripcion}) 
        print(f"{tipo} se registro correctamente.") 
        guardar_datos()  # Guardado automático
    except ValueError:
        print("Error: Por favor ingresa un monto válido.")

def ver_balance():
    total_ingresos = sum(mov["monto"] for mov in movimientos if mov["tipo"] == "Ingreso")
    total_gastos = sum(mov["monto"] for mov in movimientos if mov["tipo"] == "Gasto")
    balance = total_ingresos - total_gastos
    print(f"Total Ingresos: {formatear_monto(total_ingresos)}")
    print(f"Total Gastos: {formatear_monto(total_gastos)}")
    print(f"Balance: {formatear_monto(balance)}")

def listar_movimientos():
    if not movimientos:
        print("No hay movimientos registrados.")
        return
    for i, mov in enumerate(movimientos, start=1):
        print(f"{i}. {mov['tipo']}: {formatear_monto(mov['monto'])} | Categoría: {mov['categoria']} | Descripción: {mov['descripcion']}")


# Cargar datos al iniciar el programa
cargar_datos()

while True:
    opcion = menu()
    if opcion == 1:
        registrar_ingreso()
    elif opcion == 2:
        registrar_gasto()
    elif opcion == 3:
        ver_balance()
    elif opcion == 4:
        listar_movimientos()
    elif opcion == 5:
        borrar_todos_movimientos()
    elif opcion == 6:
        guardar_datos()  # Guardado automático al salir
        print("Gestor finalizado, adios.")
        break
    else:
        print("Opción no válida. Por favor selecciona una opción entre 1 y 6.")

