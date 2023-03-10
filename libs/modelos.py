from libs.conn_db import conectar


def importar_modelos(lista_modelos):
    for datos in lista_modelos:
        flash_id = datos[0]
        for modelo in datos[1:]:
            modelo_info = modelo.split(";")
            modelo_name = modelo_info[0]
            screen_size = modelo_info[1]
            agregar_modelo(flash_id, modelo_name, screen_size)
            print(
                f"Modelo {modelo_name} con flash_id {flash_id} y tamaño de pantalla {screen_size} agregado.")


# Funcion para buscar un modelo y obtener el flash_id
def flash_id_desde_modelos(modelo):
    mydb = conectar()
    mycursor = mydb.cursor()
    # Consulta para obtener el flash_id del modelo especificado
    query = f"SELECT flash_id FROM modelos WHERE modelo='{modelo}'"
    mycursor.execute(query)
    flash_id = mycursor.fetchone()[0]
    mycursor.close()
    mydb.close()
    return flash_id


def agregar_modelo(flash_id, modelo, screen_size):  # Funcion para agregar un nuevo modelo
    mydb = conectar()
    mycursor = mydb.cursor()
    sql = "INSERT INTO modelos (flash_id, modelo, screen_size) VALUES (%s, %s,%s)"
    val = (flash_id, modelo, screen_size)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Modelo insertado.")
    mydb.close()


def borrar_modelo(modelo):  # Funcion para borrar un modelo
    mydb = conectar()
    mycursor = mydb.cursor()
    sql = "DELETE FROM modelos WHERE modelo = %s"
    val = (modelo,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Modelo borrado.")
    mydb.close()


def mostrar_modelos():  # Funcion para mostrar todos los modelos
    mydb = conectar()
    mycursor = mydb.cursor()
    # mycursor.execute("SELECT flash_id, GROUP_CONCAT(modelo) as models FROM modelos GROUP BY flash_id ORDER BY flash_id")
    mycursor.execute(
        "SELECT flash_id, GROUP_CONCAT(modelo SEPARATOR ' - ') as models FROM modelos GROUP BY flash_id ORDER BY flash_id")
    result = mycursor.fetchall()
    for row in result:
        print(row[0] + ' : ' + row[1])
    mydb.close()


def modelo_existe(modelo):  # funcion para ver si el modelo ya existe en la basde de datos
    mydb = conectar()
    mycursor = mydb.cursor()
    sql = "SELECT modelo from modelos where modelo = %s"
    val = (modelo,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()
    if result:
        return True
    else:
        return False
