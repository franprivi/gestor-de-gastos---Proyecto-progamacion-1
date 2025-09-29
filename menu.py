movimientos = []
def menu():
    print("=== Menú Principal ===")
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Ver balance")
    print("4. Listar movimientos")
    print("5. Salir")
    
    try:
        opcion = int(input("Selecciona una opción (1 a 5): "))
        return opcion
    except ValueError:
        print("Error: Por favor ingresa un número válido entre 1 y 5.")
        return None 

def registrar_ingreso():
    try:
        monto = float(input("Ingresa el monto del ingreso: "))
        categoria = input("Ingresa una categoría para el ingreso: ")
        descripcion = input("Ingresa una descripción para el ingreso: ")
        tipo = "Ingreso"
        movimientos.append({"tipo": tipo , "monto": monto, "categoria": categoria, "descripcion": descripcion}) 
        print(f"{tipo}  registrado correctamente.") 
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
    except ValueError:
        print("Error: Por favor ingresa un monto válido.")

def ver_balance():
    total_ingresos = sum(mov["monto"] for mov in movimientos if mov["tipo"] == "Ingreso")
    total_gastos = sum(mov["monto"] for mov in movimientos if mov["tipo"] == "Gasto")
    balance = total_ingresos - total_gastos
    print(f"Total Ingresos: ${total_ingresos:.2f}")
    print(f"Total Gastos: ${total_gastos:.2f}")
    print(f"Balance: ${balance:.2f}")

def listar_movimientos():
    if not movimientos:
        print("No hay movimientos registrados.")
        return
    for i, mov in enumerate(movimientos, start=1):
        print(f"{i}. {mov['tipo']}: ${mov['monto']:.2f} | Categoría: {mov['categoria']} | Descripción: {mov['descripcion']}")


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
        print("gestor finalizado, adios.")
        break
    else:
        print("Opción no válida. Por favor selecciona una opción entre 1 y 5.")

