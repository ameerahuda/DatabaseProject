import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
from MySQLFunctions.getSQL import *

mydb = DatabaseConnection()
mycursor = mydb.cursor()

# testing getting all students
# getAllStudents()

# testing getting student by username
getStudentByUsername("'ameera0115'")