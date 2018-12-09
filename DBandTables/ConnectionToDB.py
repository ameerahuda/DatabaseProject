import mysql.connector

def DatabaseConnection():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="huda_0115",
            database="UYPdb"
        )
        return mydb

    except mysql.connector.Error as e:
        print("Unable to connect to database".format(e))
        exit(0)
