import mysql.connector


def conectar():  # Crear una conexión a la base de datos
    mydb = mysql.connector.connect(
        # Production DB
        # host="curso-php.com",
        # user="root_db",
        # password="Lanix2012$",
        # database="sql9590720",
        # charset='latin1'
        # testing DB
        host="sql9.freemysqlhosting.net",
        user="sql9590720",
        password="4W5iMJJxAI",
        database="sql9590720",
        charset='latin1'
    )
    return mydb

