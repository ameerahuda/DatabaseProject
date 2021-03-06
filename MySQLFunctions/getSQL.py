import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
from flask import Flask, render_template
import csv

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
        val = "'" + username + "'"
        statement = "SELECT * FROM Students WHERE UserName = " + val
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

        statement = "SELECT * FROM Classes WHERE IsDeleted = '0'"
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
        print studentID
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Takes, Classes WHERE Takes.ClassID = Classes.ClassID AND Takes.StudentID = '" + studentID + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        print(data)
        return render_template(filename, data=data)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN STUDENTID')
        exit(0)


def checkCourseInSession(className, sess):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Classes WHERE Classes.ClassName = %s AND Classes.Session = %s"
        vals = (className, sess)
        mycursor.execute(statement, vals)
        data = mycursor.fetchall()
        if mycursor.rowcount == 0:
            data = 0
        return data
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN STUDENTID')
        exit(0)

def studentOrPersonnel(username):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        val = "'" + username + "'"
        statement = "SELECT * FROM Students WHERE UserName = " + val
        mycursor.execute(statement)
        data = mycursor.fetchall()
        if len(data) == 0:
            statement = "SELECT * FROM Instructors WHERE UserName = " + val
            mycursor.execute(statement)
            data1 = mycursor.fetchall()
            if len(data1) == 0:
                return "invalid entry"
            else:
                return "admin entry"
        else:
            return "student entry"
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def checkIfCourseExists(courseid):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        val = "'" + courseid + "'"
        print(courseid)
        statement = "SELECT * FROM Classes WHERE ClassID = " + val
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def getInstructorByUsernameOnly(username):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Instructors WHERE UserName = '" + username + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        if mycursor.rowcount == 0:
            data = 0
        return data
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def getAllInstructors(filename):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "SELECT * FROM Instructors"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        return render_template(filename, data=data)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def getEditCourseInfo(filename, courseId):
    try:
        val = "'" + courseId + "'"
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Classes WHERE ClassID = " + val
        mycursor.execute(statement)
        data = mycursor.fetchall()

        statement = "SELECT * FROM Instructors"
        mycursor.execute(statement)
        obj = mycursor.fetchall()

        statement = "SELECT Takes.StudentID, Takes.ClassID, Students.FirstName, Students.LastName, Students.UserName " \
                    "FROM Students, Takes WHERE Takes.StudentID = Students.StudentID AND Takes.ClassID = " + val + " AND Takes.IsDeleted = '0'"
        mycursor.execute(statement)
        currStudents = mycursor.fetchall()
        print(currStudents)

        statement = "SELECT Students.StudentID, Students.FirstName, Students.LastName, Students.UserName " \
                    "FROM Students WHERE Students.StudentID NOT IN (SELECT Students.StudentID " \
                    "FROM Students, Takes WHERE Takes.StudentID = Students.StudentID AND Takes.ClassID = " + val + " AND Takes.IsDeleted = '0')"
        mycursor.execute(statement)
        otherStudents = mycursor.fetchall()
        print(otherStudents)

        return render_template(filename, data=data, obj=obj, cStu=currStudents, oStu=otherStudents)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN STUDENTID')
        exit(0)

def getCourseID(className, sess):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        print className
        print sess
        statement = "SELECT ClassID FROM Classes WHERE Classes.ClassName = %s AND Classes.Session = %s"
        vals = (className, sess)
        mycursor.execute(statement, vals)
        data = mycursor.fetchone()
        return data
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN COURSEID')
        exit(0)

def getEditStudentFromPersonnel(filename, username):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Students WHERE UserName = '" + username + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        print data

        statement = "SELECT * FROM Instructors"
        mycursor.execute(statement)
        obj = mycursor.fetchall()

        val = "'" + username + "'"
        sID = getStudentID(val)

        statement = "SELECT * FROM Mentors WHERE StudentID = '" + sID[0] + "'"
        mycursor.execute(statement)
        preMentor = mycursor.fetchall()
        print preMentor

        mData = []
        if (len(preMentor) != 0):
            statement = "SELECT * FROM Instructors WHERE InstructorID = '" + preMentor[0][0] + "'"
            mycursor.execute(statement)
            mData = mycursor.fetchall()
            print mData
        else:
            mData = [0]
            print mData

        return render_template(filename, data=data, obj = obj, mData = mData)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN STUDENTID')
        exit(0)

def getEditStudentFromPersonnel2(username):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Students WHERE UserName = '" + username + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        print data

        statement = "SELECT * FROM Instructors"
        mycursor.execute(statement)
        obj = mycursor.fetchall()

        val = "'" + username + "'"
        sID = getStudentID(val)

        statement = "SELECT * FROM Mentors WHERE StudentID = '" + sID[0] + "'"
        mycursor.execute(statement)
        preMentor = mycursor.fetchall()
        print preMentor

        if( len(preMentor) != 0 ):
            statement = "SELECT * FROM Instructors WHERE InstructorID = '" + preMentor[0][0] + "'"
            mycursor.execute(statement)
            mData = mycursor.fetchall()
            print mData

        # return render_template(filename, data=data, obj = obj)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN STUDENTID')
        exit(0)

def getCourseByInstructorAndTime(instructor, time, session):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Classes WHERE InstructorID = '" + instructor + "' AND TimeSlot = '" + time + "' AND Session = '" + session + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        if mycursor.rowcount == 0:
            data = 0
        return data
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def getCourseByRoomAndTime(building, room, time, session):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Classes WHERE Building = '" + building + "' AND RoomNumber = '" + room + "' AND TimeSlot = '" + time + "' AND Session = '" + session + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        if mycursor.rowcount == 0:
            data = 0
        return data
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def getPersonnelInfo(filename, username):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT FirstName, LastName FROM Instructors WHERE UserName = '" + username + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        print(data)
        return render_template(filename, data=data)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN USERNAME')
        exit(0)

def getPersonnelInfoOnly(username):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT FirstName, LastName FROM Instructors WHERE UserName = '" + username + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        print(data)
        return data
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO RETURN USERNAME')
        exit(0)

def getCoursesByGrade(filename, username):
    mydb = DatabaseConnection()
    mycursor = mydb.cursor()
    val = "'" + username + "'"
    student = getStudentByUsernameOnly(val)
    print student
    grade = student[0][23]
    print grade
    level = "N/A"
    if grade in ["4th", "5th"]:
        level = "4th-5th"
    if grade in ["6th", "7th" "8th"]:
        level = "6th-8th"
    if grade in ["9th", "10th", "11th", "12th"]:
        level = "9th-12th"

    statement = "SELECT * FROM Classes WHERE Classes.Level = '" + level + "'" + " AND NumberOfStudentsRegistered < Capacity"
    mycursor.execute(statement)
    data = mycursor.fetchall()
    print(data)
    return render_template(filename, data=data)

def incrementClassSize(courseid):
    mydb = DatabaseConnection()
    mycursor = mydb.cursor()
    val = "'" + courseid + "'"
    statement = "SELECT NumberOfStudentsRegistered FROM Classes WHERE ClassID = " + val
    mycursor.execute(statement)
    data = mycursor.fetchall()
    num = int(data[0][0])
    num = num + 1

    statement = "UPDATE Classes SET NumberOfStudentsRegistered = " + str(num) + " WHERE ClassID = " + val
    mycursor.execute(statement)
    mydb.commit()

def decrementClassSize(courseid):
    mydb = DatabaseConnection()
    mycursor = mydb.cursor()
    val = "'" + courseid + "'"
    statement = "SELECT NumberOfStudentsRegistered FROM Classes WHERE ClassID = " + val
    mycursor.execute(statement)
    data = mycursor.fetchall()
    num = int(data[0][0])
    num = num - 1

    statement = "UPDATE Classes SET NumberOfStudentsRegistered = " + str(num) + " WHERE ClassID = " + val
    mycursor.execute(statement)
    mydb.commit()

def getAllCoursesNoFile():
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "SELECT * FROM Classes"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        return data
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def checkIfCorrectStudentPassword(username, password):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "SELECT Password FROM Students WHERE UserName = '"+ username + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        if data[0][0] == password:
            return "Correct Password"
        else:
            return "Incorrect Password"
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def checkIfCorrectInstructorPassword(username, password):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT Password FROM Instructors WHERE UserName = '"+ username + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        if data[0][0] == password:
            return "Correct Password"
        else:
            return "Incorrect Password"
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

def getIfAlreadyInTakes(courseID, studentId):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()
        statement = "SELECT * FROM Takes WHERE StudentID = '" + studentId + "' AND ClassID = '" + courseID + "'"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        if len(data) == 0:
            return "Can input"
        else:
            return "don't input"
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)
