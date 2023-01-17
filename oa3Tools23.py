from libs import tools, modelos, flashtools, series, ordenes
from views import menu

# importar_flash_tools_list = [
# # ['flash_id', 'nombre', 'ejecutable', 'ruta_folder', 'grabar_llave', 'borrar_llave']
# ]
# importar_modelos_list = [
#     #['flash_id', 'Modelo1', 'Modelo2', 'Modelo(n)']
# ]


def agregar_orden_produccion():  # Agregar una orden de producción para poder agregar series
    print('Agregar la Orden de Produccion')
    orden_produccion = input('Orden de Produccion: ')
    modelos.mostrar_modelos()
    modelo = input("Seleccione el ID del modelo: ")
    cantidad = input('cantidad: ')
    ordenes.agregar_orden_produccion(orden_produccion, modelo, cantidad)


def agregar_flashador():  # recopilar los valores para dar de alta un flashador
    # formulario para agregar una nueva herramienta para inyectar
    print('Agregando un herramienta para inyectar')
    flash_id = input('id: ')
    nombre = input('Nombre: ')
    ejecutable = input('ejecutable: ')
    ruta_folder = input('Dame la ruta: ')
    param_grabar_llave = input('parametro para grabar: "%1"')
    param_borrar_llave = input('Parametro para eliminar llave: ')
    flashtools.agregar_flash_tool(
        flash_id, nombre, ejecutable, ruta_folder, param_grabar_llave, param_borrar_llave)


def agregar_series_a_orden():  # obtener los datos para agregar un nuevo modelo
    ordenDeProduccion = input('Ingresar orden de producción: ')
    if ordenes.orden_produccion_existe(ordenDeProduccion):
        print('Agregando serie(s) la orden producción: ' + ordenDeProduccion)
        arr_series = series.data_series_windowsID()
        for serie in arr_series:
            print(serie[0] + ' ' + serie[1] + ' ' + ordenDeProduccion)
            series.agregar_dispositivo_serie(
                serie[0], serie[1], ordenDeProduccion)
    else:
        continuar = input(
            'La orden de producción no existe, desea crearla? (s/n)')
        if continuar == 's':
            agregar_orden_produccion()
            agregar_series_a_orden()
            return


def consultar_orden_de_produccion():
    ordenes_list = ordenes.listar_ordenes_produccion()
    for orden in ordenes_list:
        print(orden[0])
    buscar_orden = input('introduce el nombre de la orden: ')
    series_en_orden = series.listar_series_en_orden_produccion(buscar_orden)
    for serie in series_en_orden:
        print(serie)
    
    
while True:
    opcion = menu.menu()
    if opcion == '0':
        # consutlar Orden de Producción
        consultar_orden_de_produccion()
        tools.pause()
    if opcion == '1':
        # Agregar Orden de Producción
        agregar_orden_produccion()
        tools.pause()
    elif opcion == '2':
        # Agregar series a la orden de produccion
        agregar_series_a_orden()
        tools.pause()
    elif opcion == '3':
        # Consutlar modelos
        modelos.mostrar_modelos()
        tools.pause()
    elif opcion == '4':
        # Consultar flashadores
        flashtools.mostrar_flash_tools()
        tools.pause()
    elif opcion == '5':
        # Agregar un modelo
        modelos.agregar_modelo()
        tools.pause()
    elif opcion == '6':
        # Agregar un flashador
        flashtools.agregar_flashador()
        tools.pause()
    elif opcion == 'q':
        break
    else:
        print("Opción inválida, intenta de nuevo.")
