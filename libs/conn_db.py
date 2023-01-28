import mysql.connector


def conectar(db=0):  # Crear una conexión a la base de datos
    if db == 1:
        mydb = mysql.connector.connect(
            # db produccion
            host="192.168.3.143",
            user="oa3admin",
            password="Lanix2012$",
            database="oa3_db",
            charset='utf8'
        )
    else:
        mydb = mysql.connector.connect(
            # db pruebas
            host="sql9.freemysqlhosting.net",
            user="sql9590720",
            password="4W5iMJJxAI",
            database="sql9590720",
            charset='latin1',
        )
    return mydb
