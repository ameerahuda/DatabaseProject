import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
from MySQLFunctions.deleteSQL import *
import uuid
import re


mydb = DatabaseConnection()
mycursor = mydb.cursor()

# testing delete from Takes table
deleteTake('a8783251f82', '95fd34bb098')

# testing delete from Mentors table
deleteMentor('0c4d6e4f5c8', 'a8783251f82')

# testing delete from Classes table
deleteClass("'95fd34bb098'")

# testing delete from Instructors table
deleteInstructor("'0c4d6e4f5c8'")

# testing delete from AdditionalInfo table
deleteAdditionalInfo("'fc32dc82-dfd'")

# testing delete from Parents table
deleteParent('d12ba374-9dd','2ec4b0b9-3f7')

# testing delete from Students table
deleteStudent("'2ec4b0b9-3f7'")
