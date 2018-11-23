import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
from MySQLFunctions.deleteSQL import *


mydb = DatabaseConnection()
mycursor = mydb.cursor()


