from views import menu
from libs import tools
from app import app_main


def submenu_produccion():
    while True:
        menu.menu_top()
        menu.menu_produccion()
        opcion = menu.menu_bottom()
        if opcion == '1':
            # Agregar Orden de Producción
            app_main.agregar_orden_produccion()
            tools.pause()
        elif opcion == '2':
            # Agregar series a la orden de produccion
            app_main.agregar_series_a_orden()
            tools.pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def submenu_administrar():
    while True:
        menu.menu_top()
        menu.menu_administrar()
        opcion = menu.menu_bottom()
        if opcion == '1':
            # Agregar Nuevas llaves a la base de datos

            tools.pause()
        elif opcion == '2':
            # Agregar nuevos modelos
            tools.pause()
        elif opcion == '3':
            # Agregar nuevos flashadores
            tools.pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def submenu_consultas():
    print("En construcción | Consultas")
    while True:
        menu.menu_top()
        menu.menu_consultas()
        opcion = menu.menu_bottom()
        if opcion == '1':
            # Agregar Nuevas llaves a la base de datos

            tools.pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def submenu_busquedas():
    print("En construcción | Busquedas")
    while True:
        menu.menu_top()
        menu.menu_busquedas()
        opcion = menu.menu_bottom()
        if opcion == '1':
            # Agregar Nuevas llaves a la base de datos

            tools.pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def submenu_ayuda():
    print("En construcción | Ayuda")
    while True:
        menu.menu_top()
        menu.menu_ayuda()
        opcion = menu.menu_bottom()
        if opcion == '1':
            # Agregar Nuevas llaves a la base de datos

            tools.pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")
