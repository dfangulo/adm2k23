import mysql.connector


def conectar():  # Crear una conexión a la base de datos
    mydb = mysql.connector.connect(
<<<<<<< HEAD
        #db produccion
        host="oa3.lanix.com",
        user="oa3admin",
        password="Lanix2012$",
        database="oa3_db",
        charset='utf8'
        
        #db pruebas
        # host="sql9.freemysqlhosting.net",
        # user="sql9590720",
        # password="4W5iMJJxAI",
        # database="sql9590720",
        # charset='latin1'
=======
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
>>>>>>> 459fef868d38d99efec80619394fde80ae77afdd
    )
    return mydb

