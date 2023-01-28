import mysql.connector


def conectar():  # Crear una conexión a la base de datos
    mydb = mysql.connector.connect(
        #db produccion
        host="oa3.lanix.com",
        user="oa3admin",
        password="Lanix2012$",
        database="oa3_db",
        charset='utf8'
    )
    return mydb

def conectar_test():
    mydb = mysql.connector.connect(   
        #db pruebas
        host="sql9.freemysqlhosting.net",
        user="sql9590720",
        password="4W5iMJJxAI",
        database="sql9590720",
        charset='latin1',
    )
    return mydb