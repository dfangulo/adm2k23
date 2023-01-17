from libs import conn_db

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

# Funcion para agregar una lsita de flashadores
def agregar_flashadores(lista):
    for flashador in lista:
        flash_id, nombre, ejecutable, ruta_folder, grabar_llave, borrar_llave = flashador
        agregar_flash_tool(flash_id, nombre, ejecutable,
                           ruta_folder, grabar_llave, borrar_llave)
        print(f"Flashador {nombre} agregado.")


# Funcion para borrar una flash_tool
def borrar_flash_tool(flash_id):
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    sql = "DELETE FROM flash_tools WHERE flash_id = %s"
    val = (flash_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Flash_tool borrada.")
    mydb.close()

# Funcion para mostrar todas las flash_tools
def mostrar_flash_tools():
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT flash_id, nombre FROM flash_tools")
    result = mycursor.fetchall()
    for row in result:
        print(row[0] + ': ' + row[1])
    mydb.close()

def obtener_ruta_folder(flash_id): #obtener el path de los flashadores 
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    # Consulta para obtener la ruta_folder del flash_id especificado
    query = f"SELECT ruta_folder FROM flash_tools WHERE flash_id='{flash_id}'"
    mycursor.execute(query)
    ruta_folder = mycursor.fetchone()[0]
    mycursor.close()
    mydb.close()
    return ruta_folder