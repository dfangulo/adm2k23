from views import menu
from libs import tools
from app import app_main

def submenu_produccion():
    while True:
        menu.menu_top()
        menu.menu_Produccion()
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
        menu.menu_Produccion()
        opcion = menu.menu_bottom()
        if opcion == '1':
            # Agregar Orden de Producción
            app_main.agregar_orden_produccion()
            tools.pause()
        elif opcion == '2':
            # Agregar series a la orden de produccion
            app_main.agregar_series_a_orden()
            tools.pause()
        elif opcion == '3':
            # Consutlar modelos
            app_main.mostrar_modelos()
            tools.pause()
        elif opcion == '4':
            # Consultar flashadores
            app_main.mostrar_flash_tools()
            tools.pause()
        elif opcion == '5':
            # Agregar un modelo
            app_main.agregar_modelo()
            tools.pause()
        elif opcion == '6':
            # Agregar un flashador
            app_main.agregar_flashador()
            tools.pause()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida, intenta de nuevo.")