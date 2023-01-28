from app.app_menu import submenu_administrar, submenu_ayuda, submenu_busquedas, submenu_consultas, submenu_produccion
from views.menu import menu_top, menu_opciones_principal, menu_bottom


while True:
    menu_top()
    menu_opciones_principal()
    opcion = menu_bottom()
    if opcion == '1':
        # Menu Produccion
        submenu_produccion()
    elif opcion == '2':
        # Menu Administrar
        submenu_administrar()
    elif opcion == '3':
        # Menu Consultas
        submenu_consultas()
    elif opcion == '4':
        # Menu Busquedas
        submenu_busquedas()
    elif opcion == '5':
        # Menu Ayuda
        submenu_ayuda()
    elif opcion == 'q':
        break
    else:
        print("Opción inválida, intenta de nuevo.")
