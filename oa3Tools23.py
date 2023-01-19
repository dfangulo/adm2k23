from app import app_menu
from views import menu


while True:
    menu.menu_top()
    menu.menu_opciones_principal()
    opcion = menu.menu_bottom()
    if opcion == '1':
        # Menu Produccion
        app_menu.submenu_produccion()
    elif opcion == '2':
        # Menu Administrar
        app_menu.submenu_administrar()
    elif opcion == '3':
        # Menu Consultas
        app_menu.submenu_consultas()
    elif opcion == '4':
        # Menu Busquedas
        app_menu.submenu_busquedas()
    elif opcion == '5':
        # Menu Ayuda
        app_menu.submenu_ayuda()
    elif opcion == 'q':
        break
    else:
        print("Opción inválida, intenta de nuevo.")
