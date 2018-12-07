import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
from flask import Flask, render_template


def getAllStudents(filename):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "SELECT * FROM Students"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        return render_template(filename, data=data)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)


# this function will get all information needed for personnel_editStudent.html includeing parent information
def getStudentByUsername(filename, username):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Students WHERE UserName = " + username
        mycursor.execute(statement)
        data = mycursor.fetchall()
        # var = "'" + data[0][0] + "'"
        # statement = "SELECT * FROM Parents WHERE StudentID = " + var
        # mycursor.execute(statement)
        # #data += mycursor.fetchall()
        # i = 0
        # result = []
        # for item in data[0]:
        #     result.append(item[i])
        #     i = i+1
        return render_template(filename, data=data)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def getStudentByUsernameOnly(username):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Students WHERE UserName = " + username
        mycursor.execute(statement)
        data = mycursor.fetchall()
        if mycursor.rowcount == 0:
            data = 0
        return data
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

# return studentID
def getStudentID(username):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT StudentID FROM Students WHERE UserName = " + username
        mycursor.execute(statement)
        data = mycursor.fetchone()
        return data
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN STUDENTID')
        exit(0)

def getAllCourses(filename):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "SELECT * FROM Classes"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        return render_template(filename, data=data)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def getStudentCoursesByUsername(filename, username):
    try:
        result = getStudentID(username)
        studentID = result[0]
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Takes, Classes WHERE Takes.ClassID = Classes.ClassID AND Takes.StudentID = '" + studentID + "'"
        mycursor.execute(statement, studentID)
        data = mycursor.fetchall()
        print(data)
        return render_template(filename, data=data)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN STUDENTID')
        exit(0)