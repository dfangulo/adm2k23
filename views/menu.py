from libs import tools

def menu_top():
    tools.clear_terminal()
    print("\n   Administracion OA3 ver:1.0")

def menu_bottom():
    print('\n\tLanix Copyright© 2023')
    opcion = input("\nSelecciona una opción: ")
    return opcion

def menu_opciones_principal():
    print("\n1. Produccion")
    print("2. Administracion")
    print("3. Consultas")
    print("4. Busquedas")
    print("5. Ayuda")
    print("q. Salir")

def menu_produccion():
    print("\n1. Agregar Orden de Produccion")
    print("2. Agregar Series a la orden")
    print("q. Salir")

def menu_administrar():
    print("\n1. Agregar Nuevas llaves")
    print("2. Agregar Nuevos Modelos")
    print("3. Agregar Nuevos Flashadores")
    print("q. Salir")