from libs.conn_db import conectar
import datetime


def agregar_dispositivo_serie(serie, windowsPkID, ordenDeProduccion):
    mydb = conectar()
    mycursor = mydb.cursor()
    current_date = datetime.datetime.now()
    sql = "INSERT INTO series (serie, windowsPkID, ordenDeProduccion, fecha) VALUES (%s, %s, %s, %s)"
    val = (serie, windowsPkID, ordenDeProduccion, current_date)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Numero de serie insertado.")
    mydb.close()


# consultar las series en una orden de producción
def listar_series_en_orden_produccion(ordenDeProduccion):
    print('informacion en OP: ' + ordenDeProduccion)
    result = []
    mydb = conectar()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM series WHERE ordenDeProduccion = %s"
    val = (ordenDeProduccion, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    mydb.close()
    return result


def data_series_windowsID():
    lines = []
    while True:
        line = input(
            "Ingrese: 'Numero Serie' 'ProductKeyID' (o 'q' para terminar): ")
        if line.strip().lower() == 'q':
            break
        if line:
            lines.append(line.split())
    return lines
