from libs import tools, modelos, flashtools, series, ordenes

# importar_flash_tools_list = [
# # ['flash_id', 'nombre', 'ejecutable', 'ruta_folder', 'grabar_llave', 'borrar_llave']
# ]
# importar_modelos_list = [
#     #['flash_id', 'Modelo1;screen_size', 'Modelo2;screen_size', 'Modelo(n);screen_size']
# ]

def agregar_flashador():  # recopilar los valores para dar de alta un flashador
    # formulario para agregar una nueva herramienta para inyectar
    print('Agregando un herramienta para inyectar')
    # obtener el flash_id consecutivo
    last_flash_id = flashtools.mostrar_ultimo_flash_id()
    flash_id = tools.increment_number(last_flash_id)
    print('Siguiente ID: ' + flash_id)
    # obtener el folder del flashador, ya deberia de estar cargado
    # en el folder ./flashtool
    flashtools.local_flashtool_folders()
    folder_flahsador = input('escribe el nombre de un folder: ')
    if folder_flahsador:
        # ver los archivos dentro del directorio
        flashtools.local_files_flashtool(folder_flahsador)
    else:
        print('folder no seleccionado')
        return
    # Copiar el folder al servidor, y ademas te da la ruta
    ruta_folder = flashtools.copy_folder_to_server(folder_flahsador)
    nombre = input('Nombre: ')
    ejecutable = input('ejecutable: ')
    param_grabar_llave = input(
        'parametro para grabar (utiliza %1 para file.bin): ')
    param_borrar_llave = input('Parametro para eliminar llave: ')
    flashador = [flash_id, nombre, ejecutable, ruta_folder,
                 param_grabar_llave, param_borrar_llave]
    print(flashador)
    # flashtools.agregar_flash_tool(flash_id, nombre, ejecutable, ruta_folder, param_grabar_llave, param_borrar_llave)


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


def agregar_orden_produccion():  # Agregar una orden de producción para poder agregar series
    print('Agregar la Orden de Produccion')
    orden_produccion = input('Orden de Produccion: ')
    modelos.mostrar_modelos()
    modelo = input("Seleccione el ID del modelo: ")
    cantidad = input('cantidad: ')
    ordenes.agregar_orden_produccion(orden_produccion, modelo, cantidad)


def consultar_orden_de_produccion():
    ordenes_list = ordenes.listar_ordenes_produccion()
    count = 0
    for orden in ordenes_list:
        print(orden[0])
    buscar_orden = input('introduce el nombre de la orden: ')
    series_en_orden = series.listar_series_en_orden_produccion(buscar_orden)
    for serie in series_en_orden:
        count += 1
        print(serie[1] + ' ' + serie[2] + ' ' + serie[3])
    print('\nOrden: ' + buscar_orden)
    print('cantidad: ' + str(count))


def agregar_modelo():  # Agregar un modelo, se necesitan modelo, flash_id, screen_size
    print('agregar modelos')
    modelos.mostrar_modelos()
    flashtools.mostrar_flash_tools()
    modelo = input('\nQue modelo quieres agregar: ')
    if modelos.modelo_existe(modelo) == True:
        print('el modelo ya existe en: ')
    else:
        screen_size = input('Tamaño de pantalla, por lo general 0.0 desktop: ')
        flashtools.mostrar_flash_tools()
        flash_id = input('Escirbe el numero del flashador: ')
        print(flash_id + ' : ' + modelo + ' : ' + screen_size)
        modelos.agregar_modelo(flash_id, modelo, screen_size)


def mostrar_modelos():
    modelos.mostrar_modelos()
    
def mostrar_flash_tools():
    flashtools.mostrar_flash_tools()