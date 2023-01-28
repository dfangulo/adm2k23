from libs.conn_db import conectar


def agregar_orden_produccion(ordenDeProduccion, modelo, cantidad):
    mydb = conectar()
    mycursor = mydb.cursor()
    sql = "INSERT INTO orden_produccion (ordenDeProduccion, modelo, cantidad) VALUES (%s, %s, %s)"
    val = (ordenDeProduccion, modelo, cantidad)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Orden de produccion insertada.")
    mydb.close()


def orden_produccion_existe(ordenDeProduccion):
    mydb = conectar()
    mycursor = mydb.cursor()
    sql = "SELECT ordenDeProduccion FROM orden_produccion WHERE ordenDeProduccion = %s"
    val = (ordenDeProduccion,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()
    if result:
        return True
    else:
        return False


# Retornar el modelo de la orden de produccion
def modelo_orden_produccion(ordenDeProduccion):
    mydb = conectar()
    mycursor = mydb.cursor()
    sql = "SELECT modelo FROM orden_produccion WHERE ordenDeProduccion = %s"
    val = (ordenDeProduccion,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()
    return result[0]


# consultar las series en una orden de producción
def consultar_orden_produccion(ordenDeProduccion):
    print('consultando la orden' + ordenDeProduccion)
    mydb = conectar()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM orden_produccion WHERE ordenDeProduccion = %s"
    val = (ordenDeProduccion,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    mydb.close()
    return result


def listar_ordenes_produccion():  # lista de las ordenes en al base de datos
    result = []
    mydb = conectar()
    mycursor = mydb.cursor()
    sql = "SELECT ordenDeProduccion FROM orden_produccion"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    mydb.close()
    return result
