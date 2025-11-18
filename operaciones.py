"""
Módulo de operaciones para el Gestor de Gastos
Contiene las funciones principales de negocio del sistema
"""

from datetime import datetime
from utils import formatear_monto
from archivos import guardar_datos, borrar_archivo_datos

def registrar_ingreso(movimientos):
    """Registra un nuevo ingreso en el sistema"""
    try:
        monto = float(input("Ingresa el monto del ingreso: "))
        if monto <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return
        
        categoria = input("Ingresa una categoría para el ingreso (usa '/' para anidar, ej: comida/salida/almuerzo): ").strip()
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
        guardar_datos(movimientos)
    except ValueError:
        print("Error: Por favor ingresa un monto válido.")

def registrar_gasto(movimientos):
    """Registra un nuevo gasto en el sistema"""
    try:
        monto = float(input("Ingresa el monto del gasto: "))
        if monto <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return

        categoria = input("Ingresa una categoría para el gasto (usa '/' para anidar, ej: comida/salida/almuerzo): ").strip()
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
        guardar_datos(movimientos)
    except ValueError:
        print("Error: Por favor ingresa un monto válido.")

def ver_balance(movimientos):
    """Muestra el balance financiero actual"""
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

def listar_movimientos(movimientos):
    """Lista todos los movimientos registrados"""
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

def editar_movimiento(movimientos):
    """Permite editar un movimiento existente"""
    if not movimientos:
        print("No hay movimientos para editar.")
        return
    
    listar_movimientos(movimientos)
    
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
        guardar_datos(movimientos)
        
    except ValueError:
        print("Error: Ingresa un número válido.")

def eliminar_movimiento(movimientos):
    """Elimina un movimiento específico"""
    if not movimientos:
        print("No hay movimientos para eliminar.")
        return
    
    listar_movimientos(movimientos)
    
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
            guardar_datos(movimientos)
        else:
            print("Operación cancelada.")
            
    except ValueError:
        print("Error: Ingresa un número válido.")

def borrar_todos_movimientos(movimientos):
    """Borra todos los movimientos de la memoria y del archivo"""
    try:
        confirmacion = input("¿Estás seguro de que quieres borrar TODOS los movimientos? (s/N): ").lower()
        if confirmacion == 's' or confirmacion == 'si':
            movimientos.clear()
            borrar_archivo_datos()
            print("Todos los movimientos han sido borrados.")
        else:
            print("Operación cancelada.")
    except Exception as e:
        print(f"Error al borrar movimientos: {e}")
