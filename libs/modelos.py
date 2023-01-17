from libs import conn_db

def importar_modelos(lista_modelos):
    print(lista_modelos)
    for datos in lista_modelos:
        flash_id = datos[0]
        for modelo in datos[1:]:
            agregar_modelo(flash_id, modelo)
            print(f"Modelo {modelo} con flash_id {flash_id} agregado.")
            

def flash_id_desde_modelos(modelo): # Funcion para buscar un modelo y obtener el flash_id
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    # Consulta para obtener el flash_id del modelo especificado
    query = f"SELECT flash_id FROM modelos WHERE modelo='{modelo}'"
    mycursor.execute(query)
    flash_id = mycursor.fetchone()[0]
    mycursor.close()
    mydb.close()
    return flash_id


def agregar_modelo(flash_id, modelo): # Funcion para agregar un nuevo modelo
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    sql = "INSERT INTO modelos (flash_id, modelo) VALUES (%s, %s)"
    val = (flash_id, modelo)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Modelo insertado.")
    mydb.close()


def borrar_modelo(modelo): # Funcion para borrar un modelo
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    sql = "DELETE FROM modelos WHERE modelo = %s"
    val = (modelo,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Modelo borrado.")
    mydb.close()


def mostrar_modelos(): # Funcion para mostrar todos los modelos
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT flash_id, GROUP_CONCAT(modelo) as models FROM modelos GROUP BY flash_id ORDER BY flash_id")
    result = mycursor.fetchall()
    for row in result:
        print(row[0] + ' : ' + row[1])
    mydb.close()
    
def mostrar_modelos_pd():
    import pandas as pd
    mydb = conn_db.conectar()
    df = pd.read_sql_query("SELECT flash_id, GROUP_CONCAT(modelo) as models FROM modelos GROUP BY flash_id ORDER BY flash_id", mydb)
    print(df)
    mydb.close()
    