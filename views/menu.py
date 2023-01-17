from libs import tools
def menu():
    tools.clear_terminal()
    print("\n   Administracion OA3 ver:1.0")
    print("\n1. Agregar Orden de Produccion")
    print("2. Agregar Series a la orden")
    print("3. Consultar modelos")
    print("4. Consultar flashadores")
    print("5. Agregar modelo")
    print("6. Agregar flashadores")
    print("q. Salir")
    print('\n\tLanix Copyright© 2023')
    opcion = input("\nSelecciona una opción: ")
    return opcion
