# insert your password wherever it says "your_password"

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "your_password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE UYPdb")