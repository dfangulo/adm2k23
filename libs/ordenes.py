from libs import conn_db


def agregar_orden_produccion(ordenDeProduccion, modelo, cantidad):
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    sql = "INSERT INTO orden_produccion (ordenDeProduccion, modelo, cantidad) VALUES (%s, %s, %s)"
    val = (ordenDeProduccion, modelo, cantidad)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Orden de produccion insertada.")
    mydb.close()
    

def orden_produccion_existe(ordenDeProduccion):
    mydb = conn_db.conectar()
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
    
def modelo_orden_produccion(ordenDeProduccion): #Retornar el modelo de la orden de produccion
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    sql = "SELECT modelo FROM orden_produccion WHERE ordenDeProduccion = %s"
    val = (ordenDeProduccion,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()
    return result[0]

def consultar_orden_produccion(ordenDeProduccion): #consultar las series en una orden de producción
    print('consultando la orden' + ordenDeProduccion)
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM orden_produccion WHERE ordenDeProduccion = %s"
    val = (ordenDeProduccion,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    mydb.close()
    return result

def listar_ordenes_produccion(): #lista de las ordenes en al base de datos
    result=[]
    mydb = conn_db.conectar()
    mycursor = mydb.cursor()
    sql = "SELECT ordenDeProduccion FROM orden_produccion"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    mydb.close()
    return result