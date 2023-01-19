from libs import tools
from app import app_menu, app_main
from views import menu

    
while True:
    menu.menu_top()
    menu.menu_opciones_principal()
    opcion = menu.menu_bottom()
    if opcion == '1':
        # Menu Produccion
        app_menu.submenu_produccion()
        tools.pause()
    elif opcion == '2':
        # Menu Administrar

        tools.pause()
    elif opcion == '3':
        # Menu Consultas

        tools.pause()
    elif opcion == '4':
        # Menu Busquedas

        tools.pause()
    elif opcion == '5':
        # Menu Ayuda

        tools.pause()
    elif opcion == 'q':
        break
    else:
        print("Opción inválida, intenta de nuevo.")
