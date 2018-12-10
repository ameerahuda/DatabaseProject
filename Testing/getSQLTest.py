import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
from MySQLFunctions.getSQL import *

mydb = DatabaseConnection()
mycursor = mydb.cursor()

# testing getting all students
# getAllStudents()

# testing getting student by username
#getStudentByUsername("'ameera0115'")

#testing getting students courses
#getStudentCoursesByUsername("'ameera0115'")

# print(studentOrPersonnel("'ameera0115'"))
#print studentOrPersonnel("'ameera0115'")

# getEditCourseInfo('2f8b7d4d-2d9')

getCoursesByGrade('Jamie51788')
