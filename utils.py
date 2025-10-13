"""
Módulo de utilidades para el Gestor de Gastos
Contiene funciones auxiliares y de formato
"""

def formatear_monto(monto):
    """Formatea el monto con formato de argentina, ejemplo: $1.541.200,23"""
    return f"${monto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida del sistema"""
    print("\n" + "="*80)
    print("                     🎯 GESTOR DE GASTOS PERSONAL 🎯")
    print("="*80)
    print("                  💰 Sistema de Control Financiero 💰")
    print("")
    print("📊 Funcionalidades disponibles:")
    print("   ✅ Registrar ingresos y gastos")
    print("   📈 Consultar balance financiero")
    print("   📋 Listar y gestionar movimientos")
    print("   ✏️  Editar y eliminar registros")
    print("   💾 Guardar datos automáticamente")
    print("")
    print("¡Controla tus finanzas de manera fácil y efectiva!")
    print("="*80)
    input("           Presiona ENTER para continuar...")
    print("\n")