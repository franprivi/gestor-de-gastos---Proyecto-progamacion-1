import json
import os
from datetime import datetime

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
    print("\n=== Menú Principal ===")
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Ver balance")
    print("4. Listar movimientos")
    print("5. Editar movimiento")
    print("6. Eliminar movimiento")
    print("7. Borrar todos los movimientos")
    print("8. Salir")
    
    try:
        opcion = int(input("Selecciona una opción (1 a 8): "))
        return opcion
    except ValueError:
        print("Error: Por favor ingresa un número válido entre 1 y 8.")
        return None

def registrar_ingreso():
    try:
        monto = float(input("Ingresa el monto del ingreso: "))
        if monto <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return
        
        categoria = input("Ingresa una categoría para el ingreso: ").strip()
        if not categoria:
            print("Error: La categoría no puede estar vacía.")
            return
        
        descripcion = input("Ingresa una descripción para el ingreso: ").strip()
        if not descripcion:
            print("Error: La descripción no puede estar vacía.")
            return
        
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        tipo = "Ingreso"
        
        movimientos.append({
            "tipo": tipo,
            "monto": monto,
            "categoria": categoria,
            "descripcion": descripcion,
            "fecha": fecha
        })
        
        print(f"{tipo} registrado correctamente.") 
        guardar_datos()
    except ValueError:
        print("Error: Por favor ingresa un monto válido.")

def registrar_gasto():
    try:
        monto = float(input("Ingresa el monto del gasto: "))
        if monto <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return
        
        categoria = input("Ingresa una categoría para el gasto: ").strip()
        if not categoria:
            print("Error: La categoría no puede estar vacía.")
            return
        
        descripcion = input("Ingresa una descripción para el gasto: ").strip()
        if not descripcion:
            print("Error: La descripción no puede estar vacía.")
            return
        
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        tipo = "Gasto"
        
        movimientos.append({
            "tipo": tipo,
            "monto": monto,
            "categoria": categoria,
            "descripcion": descripcion,
            "fecha": fecha
        })
        
        print(f"{tipo} registrado correctamente.") 
        guardar_datos()
    except ValueError:
        print("Error: Por favor ingresa un monto válido.")

def ver_balance():
    total_ingresos = sum(mov["monto"] for mov in movimientos if mov["tipo"] == "Ingreso")
    total_gastos = sum(mov["monto"] for mov in movimientos if mov["tipo"] == "Gasto")
    balance = total_ingresos - total_gastos
    
    print("\n" + "="*60)
    print("BALANCE FINANCIERO")
    print("="*60)
    print(f"Total Ingresos: {formatear_monto(total_ingresos)}")
    print(f"Total Gastos:   {formatear_monto(total_gastos)}")
    print("-"*60)
    print(f"Balance:        {formatear_monto(balance)}")
    print("="*60)

def listar_movimientos():
    if not movimientos:
        print("No hay movimientos registrados.")
        return
    
    print("\n" + "="*100)
    print(f"{'#':<4} {'Tipo':<10} {'Monto':<18} {'Categoría':<20} {'Descripción':<30} {'Fecha':<17}")
    print("="*100)
    
    for i, mov in enumerate(movimientos, start=1):
        fecha = mov.get('fecha', 'N/A')
        print(f"{i:<4} {mov['tipo']:<10} {formatear_monto(mov['monto']):<18} "
              f"{mov['categoria']:<20} {mov['descripcion']:<30} {fecha:<17}")
    
    print("="*100)
    print(f"Total de movimientos: {len(movimientos)}")

def editar_movimiento():
    """Permite editar un movimiento existente"""
    if not movimientos:
        print("No hay movimientos para editar.")
        return
    
    listar_movimientos()
    
    try:
        indice = int(input("\nIngresa el número del movimiento a editar: ")) - 1
        
        if indice < 0 or indice >= len(movimientos):
            print("Error: Número de movimiento inválido.")
            return
        
        mov = movimientos[indice]
        print(f"\nEditando: {mov['tipo']} - {formatear_monto(mov['monto'])}")
        print("(Presiona Enter para mantener el valor actual)")
        
        # Editar monto
        nuevo_monto = input(f"Nuevo monto (actual: {formatear_monto(mov['monto'])}): $")
        if nuevo_monto.strip():
            try:
                monto_float = float(nuevo_monto)
                if monto_float > 0:
                    mov['monto'] = monto_float
                else:
                    print("Monto inválido, se mantiene el anterior.")
            except ValueError:
                print("Monto inválido, se mantiene el anterior.")
        
        # Editar categoría
        nueva_categoria = input(f"Nueva categoría (actual: {mov['categoria']}): ")
        if nueva_categoria.strip():
            mov['categoria'] = nueva_categoria
        
        # Editar descripción
        nueva_descripcion = input(f"Nueva descripción (actual: {mov['descripcion']}): ")
        if nueva_descripcion.strip():
            mov['descripcion'] = nueva_descripcion
        
        print("Movimiento editado correctamente.")
        guardar_datos()
        
    except ValueError:
        print("Error: Ingresa un número válido.")

def eliminar_movimiento():
    """Elimina un movimiento específico"""
    if not movimientos:
        print("No hay movimientos para eliminar.")
        return
    
    listar_movimientos()
    
    try:
        indice = int(input("\nIngresa el número del movimiento a eliminar: ")) - 1
        
        if indice < 0 or indice >= len(movimientos):
            print("Error: Número de movimiento inválido.")
            return
        
        mov = movimientos[indice]
        confirmacion = input(f"¿Confirmas eliminar: {mov['tipo']} - {formatear_monto(mov['monto'])}? (s/N): ").lower()
        
        if confirmacion == 's' or confirmacion == 'si':
            movimientos.pop(indice)
            print("Movimiento eliminado correctamente.")
            guardar_datos()
        else:
            print("Operación cancelada.")
            
    except ValueError:
        print("Error: Ingresa un número válido.")


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
        editar_movimiento()
    elif opcion == 6:
        eliminar_movimiento()
    elif opcion == 7:
        borrar_todos_movimientos()
    elif opcion == 8:
        guardar_datos()
        print("Gestor finalizado, adios.")
        break
    else:
        print("Opción no válida. Por favor selecciona una opción entre 1 y 8.")
