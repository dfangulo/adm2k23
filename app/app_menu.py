from views.menu import menu_top, menu_produccion, menu_administrar, menu_ayuda, menu_bottom, menu_busquedas, menu_consultas
from libs.tools import pause
from app import app_main


def submenu_produccion():
    while True:
        menu_top()
        menu_produccion()
        opcion = menu_bottom()
        if opcion == '1':
            # Agregar Orden de Producción
            app_main.agregar_orden_produccion()
            pause()
        elif opcion == '2':
            # Agregar series a la orden de produccion
            app_main.agregar_series_a_orden()
            pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def submenu_administrar():
    while True:
        menu_top()
        menu_administrar()
        opcion = menu_bottom()
        if opcion == '1':
            # Agregar Nuevas llaves a la base de datos

            pause()
        elif opcion == '2':
            # Agregar nuevos modelos
            pause()
        elif opcion == '3':
            # Agregar nuevos flashadores
            pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def submenu_consultas():
    print("En construcción | Consultas")
    while True:
        menu_top()
        menu_consultas()
        opcion = menu_bottom()
        if opcion == '1':
            #Mostrar todas las series en lal base de datos

            pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def submenu_busquedas():
    print("En construcción | Busquedas")
    while True:
        menu_top()
        menu_busquedas()
        opcion = menu_bottom()
        if opcion == '1':
            # mostrar una salida con las llaves de una orden

            pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def submenu_ayuda():
    print("En construcción | Ayuda")
    while True:
        menu_top()
        menu_ayuda()
        opcion = menu_bottom()
        if opcion == '1':
            # Mostrar el menu de ayuda

            pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")
