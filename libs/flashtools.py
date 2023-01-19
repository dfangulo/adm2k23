import os
import shutil
from libs import conn_db
from smb.SMBConnection import SMBConnection

# variables>
info_local_files = {
    'flashtool_path': '.\\flashtool\\'
}
info_server = {
    'server': {
        'name': 'WIN-JCJ6O9DP4T7',
        'ip': '192.168.2.100'
    },
    'username': 'oa3admin',
    'password': 'OA#2020$',
    'share': 'server',
    'flashtool_path': '\\flashtool\\'
    # \\192.168.2.100\server\flashtool
}


# Funcion para agregar una nueva flash_tool
def agregar_flash_tool(flash_id, nombre, ejecutable, ruta_folder, grabar_llave, borrar_llave):
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    sql = "INSERT INTO flash_tools (flash_id, nombre, ejecutable, ruta_folder, grabar_llave, borrar_llave) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (flash_id, nombre, ejecutable,
           ruta_folder, grabar_llave, borrar_llave)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Flash_tool insertada.")
    mydb.close()


def agregar_flashadores(lista):  # Funcion para agregar una lsita de flashadores
    for flashador in lista:
        flash_id, nombre, ejecutable, ruta_folder, grabar_llave, borrar_llave = flashador
        agregar_flash_tool(flash_id, nombre, ejecutable,
                           ruta_folder, grabar_llave, borrar_llave)
        print(f"Flashador {nombre} agregado.")


def borrar_flash_tool(flash_id):  # Funcion para borrar una flash_tool
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    sql = "DELETE FROM flash_tools WHERE flash_id = %s"
    val = (flash_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Flash_tool borrada.")
    mydb.close()


def mostrar_flash_tools():  # Funcion para mostrar todas las flash_tools
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT flash_id, nombre FROM flash_tools")
    result = mycursor.fetchall()
    for row in result:
        print(row[0] + ': ' + row[1])
    mydb.close()


def mostrar_ultimo_flash_id(): # Funcion para obtener el ultimo flash_id
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT MAX(flash_id) FROM flash_tools")
    result = mycursor.fetchone()
    #print(result[0])
    mydb.close()
    return result[0]


def obtener_ruta_folder(flash_id):  # obtener el path de los flashadores
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    # Consulta para obtener la ruta_folder del flash_id especificado
    query = f"SELECT ruta_folder FROM flash_tools WHERE flash_id='{flash_id}'"
    mycursor.execute(query)
    ruta_folder = mycursor.fetchone()[0]
    mycursor.close()
    mydb.close()
    return ruta_folder


def copy_folder_to_server(new_folder): #Copiar folder de flashador local a servidor
    source_folder_path = info_local_files['flashtool_path'] + new_folder
    destination_folder_path = '\\\\' + \
        info_server['server']['ip'] + '\\' + \
        info_server['share'] + info_server['flashtool_path'] + new_folder
    try:
        conn = SMBConnection(info_server['username'], info_server['password'], "localhost",
                             info_server['server']['name'], use_ntlm_v2=True)
        conn.connect(info_server['server']['ip'], 139)

        folder_name = os.path.basename(new_folder)
        print(folder_name)
        if folder_name in [entry.filename for entry in conn.listPath(info_server['share'], info_server['flashtool_path'])]:
            print(
                f"The folder {folder_name} already exists in {info_server['flashtool_path']}")
        else:
            # copy the folder to server
            shutil.copytree(source_folder_path, destination_folder_path)
            print(
                f"Folder {folder_name} copied successfully to {info_server['flashtool_path']}")
    except Exception as e:
        print(f'Error {e}')
        conn.close()
    conn.close()
    return destination_folder_path


def local_flashtool_folders():  # imprimir una lista de los flashadores en el folder ./flashtool
    folder_list = os.listdir(info_local_files['flashtool_path'])
    for folder in folder_list:
        print(folder)


def local_files_flashtool(folder):# listar los archivos para selecionar el ejecutable
    dir_path = info_local_files['flashtool_path'] + folder
    if os.path.exists(dir_path):
        files = [file for file in os.listdir(
            dir_path) if file.endswith(".exe")]

        if files:
            print("List of exe files:")
            for file in files:
                print(f"- {os.path.basename(file)}")
        else:
            print("No exe files found in the directory.")
    else:
        print(f"The directory {dir_path} does not exist.")
