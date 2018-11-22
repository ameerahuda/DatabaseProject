# uncomment each table sql one at a time and then run
# insert your password wherever it says "your_password"

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Chivas14",
    database = "UYPdb"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE Students (StudentID VARCHAR(255), DateOfRegistration DATE, AcceptedStatus VARCHAR(255), "
#                  "FirstName VARCHAR(255), LastName VARCHAR(255), "
#                  "MiddleInitial VARCHAR(255), Suffix VARCHAR(255), PreferredName VARCHAR(255), DateOfBirth DATE, "
#                  "Gender VARCHAR(255), Race VARCHAR(255), Address VARCHAR(255), City VARCHAR(255), State VARCHAR(255), "
#                  "Zip VARCHAR(255), Email VARCHAR(255), PhoneNumber VARCHAR(255), DisabilityInfo VARCHAR(255), "
#                  "HealthConditions VARCHAR(255), Siblings VARCHAR(255), SchoolName VARCHAR(255), SchoolDistrict VARCHAR(255), "
#                  "SchoolType VARCHAR(255), GradeInFall VARCHAR(255), ExpectedHighSchool VARCHAR(255), "
#                  "ExpectedGradYear VARCHAR(255), GT VARCHAR(255), ELL VARCHAR(255), "
#                  "CONSTRAINT PK_Students PRIMARY KEY (StudentID))")
#
# mycursor.execute("CREATE TABLE Parents (ParentID VARCHAR(255), StudentID VARCHAR(255), FirstName VARCHAR(255), "
#                  "LastName VARCHAR(255), Address VARCHAR(255), City VARCHAR(255), State VARCHAR(255), "
#                  "Zip VARCHAR(255), Email VARCHAR(255), CellPhoneNumber VARCHAR(255), WorkPhoneNumber VARCHAR(255), "
#                  "HomePhoneNumber VARCHAR(255), "
#                  "CONSTRAINT PK_Parents PRIMARY KEY (ParentID, StudentID), "
#                  "CONSTRAINT FK0_Parents FOREIGN KEY (StudentID) REFERENCES Students(StudentID))")
#
# mycursor.execute("CREATE TABLE AdditionalInfo (StudentID VARCHAR(255), YearAccepted VARCHAR(255), GradeWhenAccepted VARCHAR(255), "
#                  "Status VARCHAR(255), FundingStatus VARCHAR(255), GrantName VARCHAR(255), NationalClearingHouse VARCHAR(255), "
#                  "CONSTRAINT PK_AdditionalInfo PRIMARY KEY (StudentID), "
#                  "CONSTRAINT FK0_AdditionalInfo FOREIGN KEY (StudentID) REFERENCES Students(StudentID))")
#
# mycursor.execute("CREATE TABLE Instructors (InstructorID VARCHAR(255), FirstName VARCHAR(255), LastName VARCHAR(255), "
#                  "CONSTRAINT PK_Instructor PRIMARY KEY (InstructorID))")
#
# mycursor.execute("CREATE TABLE Classes (ClassID VARCHAR(255), ClassName VARCHAR(255), InstructorID VARCHAR(255), "
#                  "Session VARCHAR(255), Level VARCHAR(255), TimeSlot VARCHAR(255), Building VARCHAR(255), "
#                  "RoomNumber VARCHAR(255), Capacity VARCHAR(255), NumberOfStudentsRegistered VARCHAR(255), "
#                  "NumberOfStudentsWaitlisted VARCHAR (255), "
#                  "CONSTRAINT PK_Classes PRIMARY KEY (ClassID), "
#                  "CONSTRAINT FK0_Classes FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID))")
#
# mycursor.execute("CREATE TABLE Mentors (InstructorID VARCHAR(255), StudentID VARCHAR(255), "
#                  "CONSTRAINT PK_Mentors PRIMARY KEY (InstructorID, StudentID),"
#                  "CONSTRAINT FK0_Mentors FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID),"
#                  "CONSTRAINT FK1_Mentors FOREIGN KEY (StudentID) REFERENCES Students(StudentID))")
#
# mycursor.execute("CREATE TABLE Takes (StudentID VARCHAR(255), ClassID VARCHAR(255), "
#                  "CONSTRAINT PK_Takes PRIMARY KEY (StudentID, ClassID),"
#                  "CONSTRAINT FK0_Takes FOREIGN KEY (StudentID) REFERENCES Students(StudentID),"
#                  "CONSTRAINT FK1_Takes FOREIGN KEY (ClassID) REFERENCES Classes(ClassID))")

mycursor.execute("SHOW TABLES")

for tb in mycursor:
     print(tb)


