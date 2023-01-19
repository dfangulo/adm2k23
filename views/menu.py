from libs import tools
import msvcrt


def menu_top():
    tools.clear_terminal()
    print("\n   Administracion OA3 ver:1.0-beta")


def menu_bottom():
    print('\n\tLanix Copyright© 2023')
    print("\nSelecciona una opción: ")
    opcion = msvcrt.getch().decode('utf-8')  # Lee un caracter del teclado
    return opcion


def menu_opciones_principal():
    print("\nMenu: Principal")
    print("\n1. Produccion")
    print("2. Administracion")
    print("3. Consultas")
    print("4. Busquedas")
    print("5. Ayuda")
    print("q. Salir")


def menu_produccion():
    print("\nMenu: Produccion")
    print("\n1. Agregar Orden de Produccion")
    print("2. Agregar Series a la orden")
    print("q. Atras")


def menu_administrar():
    print("\nMenu: Administrar")
    print("\n1. Agregar Nuevas llaves")
    print("2. Agregar Nuevos Modelos")
    print("3. Agregar Nuevos Flashadores")
    print("q. Atras")


def menu_consultas():
    print("\nMenu: Consultas")
    print("\n1. Llaves disponibles")
    print("2. Ordenes de producción")
    print("3. Series de Orden de Produccion")
    print("4. Modelos")
    print("5. Flashadores")
    print("q. Atras")


def menu_busquedas():
    print("\nMenu: Busquedas")
    print("\n1. Series")
    print("2. llaves")
    print("3. modelos")
    print("4. flashador")
    print("q. Atras")


def menu_ayuda():
    print("\nMenu: Ayuda")
    print("\n1. Agregar un modelo")
    print("2. Agregar un Flashador")
    print("3. Agregar una orden de produccion")
    print("4. Agregar series a la orden")
    print("5. agregar nuevas llaves para inyeccion")
    print("q. Atras")
