import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
from Classes.Objects import *

def insertStudent(Student):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "INSERT INTO Students (StudentID, DateOfRegistration, AcceptedStatus, FirstName, LastName, MiddleInitial, " \
                    "Suffix, PreferredName, DateOfBirth, Gender, Race, Address, City, State, Zip, Email, PhoneNumber, " \
                    "DisabilityInfo, HealthConditions, Siblings, SchoolName, SchoolDistrict, SchoolType, GradeInFall, " \
                    "ExpectedHighSchool, ExpectedGradYear, GT, ELL, ApprovedBy, UserName, Password, IsDeleted) VALUES " \
                    "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(statement, (Student.id, Student.DateOfRegisteration, Student.AceeptedStatus, Student.FirstName,
                                     Student.LasName, Student.MiddleInitial, Student.Suffix, Student.PreferredName,
                                     Student.DateOfBirth, Student.Gender, Student.Race, Student.Address, Student.City,
                                     Student.State, Student.Zip, Student.Email, Student.PhoneNumber, Student.DisabilityInfo,
                                     Student.HealthConditions, Student.Siblings, Student.SchoolName, Student.SchoolDistrict,
                                     Student.SchoolType, Student.GradeInFall, Student.ExpectedHighSchool, Student.ExpectedGradYear,
                                     Student.GT, Student.ELL, Student.ApprovedBy, Student.UserName, Student.Password, Student.IsDeleted))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO INSERT: TRY AGAIN')
        exit(0)

def insertParent(Parent):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "INSERT INTO Parents (ParentID, StudentID, FirstName, LastName, Address, City, State, Zip, Email, " \
                    "CellPhoneNumber, WorkPhoneNumber, HomePhoneNumber, IsDeleted) VALUES " \
                    "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(statement, (Parent.ParentID, Parent.StudentID, Parent.FirstName, Parent.LastName, Parent.Address,
                                     Parent.City, Parent.State, Parent.Zip, Parent.Email, Parent.CellPhoneNumber,
                                     Parent.WorkPhoneNumber, Parent.HomePhoneNumber, Parent.IsDeleted))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO INSERT: TRY AGAIN')
        exit(0)

def insertAdditionalInfo(AdditionalInformation):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "INSERT INTO AdditionalInfo (StudentID, YearAccepted, GradeWhenAccepted, Status, FundingStatus, " \
                    "GrantName, NationalClearingHouse, IsDeleted) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(statement, (AdditionalInformation.StudentID, AdditionalInformation.YearAccepted,
                                     AdditionalInformation.GradeWhenAccepted, AdditionalInformation.Status,
                                     AdditionalInformation.FundingStatus, AdditionalInformation.GrantName,
                                     AdditionalInformation.NationalClearingHouse, AdditionalInformation.IsDeleted))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO INSERT: TRY AGAIN')
        exit(0)

def insertInstructor(Instructor):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "INSERT INTO Instructors (InstructorID, FirstName, LastName, UserName, Password, IsDeleted) " \
                    "VALUES (%s,%s,%s,%s,%s,%s)"
        mycursor.execute(statement, (Instructor.InstructorID, Instructor.FirstName, Instructor.LastName,
                                     Instructor.Username, Instructor.Password, Instructor.IsDeleted))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO INSERT: TRY AGAIN')
        exit(0)

def insertClass(Class):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "INSERT INTO Classes (ClassID, ClassName, InstructorID, Session, Level, TimeSlot, Building, " \
                    "RoomNumber, Capacity, NumberOfStudentsRegistered, NumberOfStudentsWaitlisted, IsDeleted)" \
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(statement, (Class.ClassID, Class.ClassName, Class.InstructorID, Class.Session, Class.Level,
                                     Class.TimeSlot, Class.Building, Class.RoomNumber, Class.Capacity,
                                     Class.NumOfStudentsRegistered, Class.NumOfStudentsWaitlisted, Class.IsDeleted))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO INSERT: TRY AGAIN')
        exit(0)

def insertMentor(Mentor):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "INSERT INTO Mentors (InstructorID, StudentID, IsDeleted) VALUES (%s,%s,%s)"
        mycursor.execute(statement, (Mentor.InstructorID, Mentor.StudentID, Mentor.IsDeleted))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO INSERT: TRY AGAIN')
        exit(0)

def insertTake(Take):
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "INSERT INTO Takes (StudentID, ClassID, IsDeleted) VALUES (%s,%s,%s)"
        mycursor.execute(statement, (Take.StudentID, Take.ClassID, Take.IsDeleted))
        mydb.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO INSERT: TRY AGAIN')
        exit(0)