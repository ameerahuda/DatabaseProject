import mysql.connecton
from DBandTables.ConnectionToDB import DatabaseConnection
from Classes.Objects import *

def deleteStudent(studentID):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "UPDATE Students SET isDeleted = 1 WHERE StudentID = " + studentID
        mycursor.execute(statement)
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print e
        print 'FAILED TO INSERT: TRY AGAIN'
        exit(0)

def deleteParent(parentID, studentID):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "UPDATE Parents SET isDeleted = 1 WHERE ParentID = %s AND StudentID = %s"
        mycursor.execute(statement, (parentID, studentID))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print e
        print 'FAILED TO INSERT: TRY AGAIN'
        exit(0)

def deleteAdditionalInfo(studentID):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "UPDATE AdditionalInfo SET isDeleted = 1 WHERE StudentID = " + studentID
        mycursor.execute(statement)
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print e
        print 'FAILED TO INSERT: TRY AGAIN'
        exit(0)

def deleteInstructor(instructorID):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "UPDATE Instructors SET isDeleted = 1 WHERE InstructorID = " + instructorID
        mycursor.execute(statement)
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print e
        print 'FAILED TO INSERT: TRY AGAIN'
        exit(0)

def deleteClass(classID):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "UPDATE Classes SET isDeleted = 1 WHERE ClassID = " + classID
        mycursor.execute(statement)
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print e
        print 'FAILED TO INSERT: TRY AGAIN'
        exit(0)

def deleteMentor(instructorID, studentID):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "UPDATE Mentors SET isDeleted = 1 WHERE InstructorID = %s AND StudentID = %s"
        mycursor.execute(statement, (instructorID, studentID))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print e
        print 'FAILED TO INSERT: TRY AGAIN'
        exit(0)

def deleteTake(studentID, classID):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "UPDATE Takes SET isDeleted = 1 WHERE StudentID = %s AND ClassID = %s"
        mycursor.execute(statement, (studentID, classID))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print e
        print 'FAILED TO INSERT: TRY AGAIN'
        exit(0)